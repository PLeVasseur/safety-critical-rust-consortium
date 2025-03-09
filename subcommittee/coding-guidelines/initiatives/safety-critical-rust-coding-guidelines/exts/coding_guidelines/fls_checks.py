# SPDX-License-Identifier: MIT OR Apache-2.0
# SPDX-FileCopyrightText: The Coding Guidelines Subcommittee Contributors

import requests
import logging
import re
from sphinx.errors import SphinxError
from sphinx_needs.data import SphinxNeedsData

# Get the Sphinx logger
logger = logging.getLogger('sphinx')
fls_url = "https://spec.ferrocene.dev/"

class FLSValidationError(SphinxError):
    category = "FLS Validation Error"

def check_fls(app, env):
    """Main checking function for FLS validation"""
    # First make sure all guidelines have correctly formatted FLS IDs
    check_fls_exists_and_valid_format(app, env)
    
    # Gather all FLS paragraph IDs from the specification
    fls_ids = gather_fls_paragraph_ids(fls_url)
    
    # Check if all referenced FLS IDs exist
    check_fls_ids_correct(app, env, fls_ids)
    
    # Read the ignore list
    fls_id_ignore_list = read_fls_ignore_list(app)
    
    # Insert coverage information into fls_ids
    insert_fls_coverage(app, env, fls_ids)
    
    # Calculate and report coverage
    coverage_data = calculate_fls_coverage(fls_ids, fls_id_ignore_list)
    
    # Log coverage report
    log_coverage_report(coverage_data)


def read_fls_ignore_list(app):
    """Read the list of FLS IDs to ignore from a file"""
    ignore_file_path = app.confdir / 'fls_ignore_list.txt'
    ignore_list = []
    
    if ignore_file_path.exists():
        logger.info(f"Reading FLS ignore list from {ignore_file_path}")
        with open(ignore_file_path, 'r') as f:
            for line in f:
                # Remove comments and whitespace
                line = line.split('#')[0].strip()
                if line:
                    ignore_list.append(line)
        logger.info(f"Loaded {len(ignore_list)} FLS IDs to ignore")
    else:
        logger.warning(f"No FLS ignore list found at {ignore_file_path}")
    
    return ignore_list


def check_fls_exists_and_valid_format(app, env):
    logger.debug("check_fls_exists_and_valid_format")

    data = SphinxNeedsData(env)

    needs = data.get_needs_view()
    logger.debug(f"Checking needs {needs!r}")

    # Regular expression for FLS ID validation
    # Format: fls_<12 alphanumeric chars including upper and lowercase>
    fls_pattern = re.compile(r'^fls_[a-zA-Z0-9]{12}$')
    for need_id, need in needs.items():
        logger.debug(f"ID: {need_id}, Need: {need}")

        if need.get('type') == 'guideline':
            fls_value = need.get("fls")
            
            # Check if fls field exists and is not empty
            if fls_value is None:
                msg = f"Need {need_id} has no fls field"
                logger.error(msg)
                raise FLSValidationError(msg)
                
            if fls_value == "":
                msg = f"Need {need_id} has empty fls field"
                logger.error(msg)
                raise FLSValidationError(msg)
            
            # Validate FLS ID format
            if not fls_pattern.match(fls_value):
                msg = f"Need {need_id} has invalid fls format: '{fls_value}'. Expected format: fls_ followed by 12 alphanumeric characters"
                logger.error(msg)
                raise FLSValidationError(msg)

    
def check_fls_ids_correct(app, env, fls_ids):
    """
    Check that all FLS IDs referenced in guidelines actually exist in the specification.
    
    Args:
        app: The Sphinx application
        env: The Sphinx environment
        fls_ids: Dictionary of FLS paragraph IDs mapped to their source URLs
    """
    logger.debug("check_fls_ids_correct")
    data = SphinxNeedsData(env)
    needs = data.get_needs_view()
    
    # Track any errors found
    invalid_ids = []
    
    # Check each guideline's FLS reference
    for need_id, need in needs.items():
        if need.get('type') == 'guideline':
            fls_value = need.get("fls")
            
            # Skip needs we already validated format for
            if fls_value is None or fls_value == "":
                continue
                
            # Check if the FLS ID exists in the gathered IDs
            if fls_value not in fls_ids:
                invalid_ids.append((need_id, fls_value))
                logger.warning(f"Need {need_id} references non-existent FLS ID: '{fls_value}'")
    
    # Raise error if any invalid IDs were found
    if invalid_ids:
        error_message = "The following needs reference non-existent FLS IDs:\n"
        for need_id, fls_id in invalid_ids:
            error_message += f"  - Need {need_id} references '{fls_id}'\n"
        logger.error(error_message)
        raise FLSValidationError(error_message)
    
    logger.info("All FLS references in guidelines are valid")


def gather_fls_paragraph_ids(base_url):
    """
    Gather all Ferrocene Language Specification paragraph IDs by crawling the specification.
    
    Args:
        base_url: The base URL of the Ferrocene Language Specification
        
    Returns:
        A dictionary mapping paragraph IDs to dictionaries containing:
        - url: Direct URL with fragment identifier
        - section_id: The section identifier (e.g., "4.3.1:9")
    """
    logger.info("Gathering FLS paragraph IDs from %s", base_url)
    
    # Dictionary to store paragraph IDs and their metadata
    paragraph_ids = {}
    
    # Set to track visited URLs to avoid duplicates
    visited_urls = set()
    
    # Queue of URLs to process
    urls_to_process = [base_url]
    
    # Regular expression to find paragraph IDs and their section IDs
    paragraph_id_pattern = re.compile(r'<span class="spec-paragraph-id" id="(fls_[a-zA-Z0-9]{12})">([^<]+)</span>')
    
    # Regular expression to find links to other pages
    link_pattern = re.compile(r'<a class="reference internal" href="([^"#]+\.html)"')
    
    while urls_to_process:
        current_url = urls_to_process.pop(0)
        
        # Skip if already visited
        if current_url in visited_urls:
            continue
        
        visited_urls.add(current_url)
        logger.debug("Processing URL: %s", current_url)
        
        try:
            # Normalize URL
            page_url = current_url
            if not page_url.startswith("http"):
                page_url = base_url + page_url
            
            # Fetch and decode page content
            response = requests.get(page_url)
            response.raise_for_status()  # Raise exception for HTTP errors
            page_content = response.text
            
            # Extract paragraph IDs and their section IDs
            for match in paragraph_id_pattern.finditer(page_content):
                paragraph_id = match.group(1)
                section_id = match.group(2).strip()
                
                # Create direct link to the paragraph by adding the ID as a fragment
                direct_url = f"{page_url}#{paragraph_id}"
                
                # Store both URL and section ID
                paragraph_ids[paragraph_id] = {
                    "url": direct_url,
                    "section_id": section_id
                }
            
            # Find links to other pages
            for match in link_pattern.finditer(page_content):
                href = match.group(1)
                # Skip non-HTML links, index, and search pages
                if (href not in visited_urls and 
                    not href.startswith("#") and 
                    href != "index.html" and 
                    href != "search.html"):
                    urls_to_process.append(href)
                    
        except requests.exceptions.RequestException as e:
            logger.error("Error fetching %s: %s", page_url, e)
    
    logger.info("Found %d FLS paragraph IDs", len(paragraph_ids))
    return paragraph_ids

def insert_fls_coverage(app, env, fls_ids):
    """
    Enrich the fls_ids with whether each FLS ID is covered by coding guidelines
    
    Args:
        app: The Sphinx application
        env: The Sphinx environment
        fls_ids: Dictionary of FLS paragraph IDs with metadata
    """
    logger.debug("Inserting FLS coverage data")
    data = SphinxNeedsData(env)
    needs = data.get_needs_view()
    
    # Initialize coverage for all FLS IDs
    for fls_id in fls_ids:
        fls_ids[fls_id]['covered'] = False
        fls_ids[fls_id]['covering_needs'] = []  # List to store all covering guidelines
        
        # Extract chapter information from section_id (e.g., "4.3.1:9" -> chapter 4)
        section_parts = fls_ids[fls_id]['section_id'].split('.')
        if section_parts and section_parts[0].isdigit():
            chapter = int(section_parts[0])
            fls_ids[fls_id]['chapter'] = chapter
        else:
            # Handle appendices or other non-standard formats
            first_char = fls_ids[fls_id]['section_id'][0] if fls_ids[fls_id]['section_id'] else None
            if first_char and first_char.isalpha():
                # For appendices like "A.1.1", use the letter as chapter
                fls_ids[fls_id]['chapter'] = first_char
            else:
                fls_ids[fls_id]['chapter'] = 'unknown'
    
    # Mark covered FLS IDs
    unique_covered_ids = set()
    total_references = 0
    
    for need_id, need in needs.items():
        if need.get('type') == 'guideline':
            fls_value = need.get("fls")
            if fls_value and fls_value in fls_ids:
                fls_ids[fls_value]['covered'] = True
                fls_ids[fls_value]['covering_needs'].append(need_id)
                unique_covered_ids.add(fls_value)
                total_references += 1
    
    logger.info(f"Found {total_references} references to FLS IDs in guidelines")
    logger.info(f"Found {len(unique_covered_ids)} unique FLS IDs covered by guidelines")
    return fls_ids

def calculate_fls_coverage(fls_ids, fls_id_ignore_list):
    """
    Calculate coverage statistics for FLS IDs
    
    Args:
        fls_ids: Dictionary of FLS paragraph IDs with metadata, including coverage status
        fls_id_ignore_list: List of FLS IDs to ignore in coverage calculations
    
    Returns:
        Dictionary containing coverage statistics
    """
    logger.debug("Calculating FLS coverage statistics")
    
    # Track statistics
    total_ids = 0
    covered_ids = 0
    ignored_ids = 0
    
    # Organize by chapter
    chapters = {}
    
    # Process each FLS ID
    for fls_id, metadata in fls_ids.items():
        chapter = metadata.get('chapter', 'unknown')
        
        # Initialize chapter data if needed
        if chapter not in chapters:
            chapters[chapter] = {
                'total': 0,
                'covered': 0,
                'ignored': 0,
                'ids': []
            }
        
        # Add to chapter's ID list
        chapters[chapter]['ids'].append(fls_id)
        chapters[chapter]['total'] += 1
        total_ids += 1
        
        # Check if ID should be ignored
        if fls_id in fls_id_ignore_list:
            ignored_ids += 1
            chapters[chapter]['ignored'] += 1
            # Mark as ignored in the original data structure too
            fls_ids[fls_id]['ignored'] = True
        else:
            fls_ids[fls_id]['ignored'] = False
            
            # Count coverage if not ignored
            if metadata.get('covered', False):
                covered_ids += 1
                chapters[chapter]['covered'] += 1
    
    # Calculate coverage percentages
    effective_total = total_ids - ignored_ids
    overall_coverage = (covered_ids / effective_total * 100) if effective_total > 0 else 0
    
    # Calculate chapter coverage
    chapter_coverage = {}
    for chapter, data in chapters.items():
        effective_chapter_total = data['total'] - data['ignored']
        
        if effective_chapter_total == 0:
            # All IDs in this chapter are ignored
            chapter_coverage[chapter] = "IGNORED"
        else:
            chapter_coverage[chapter] = (data['covered'] / effective_chapter_total * 100)
    
    # Sort chapters by custom logic to handle mixed types
    def chapter_sort_key(chapter):
        if isinstance(chapter, int):
            return (0, chapter)  # Sort integers first, by their value
        elif isinstance(chapter, str) and chapter.isalpha():
            return (1, chapter)  # Sort letters second, alphabetically
        else:
            return (2, str(chapter))  # Sort anything else last
    
    sorted_chapters = sorted(chapters.keys(), key=chapter_sort_key)
    
    # Prepare result
    coverage_data = {
        'total_ids': total_ids,
        'covered_ids': covered_ids,
        'ignored_ids': ignored_ids,
        'effective_total': effective_total,
        'overall_coverage': overall_coverage,
        'chapters': sorted_chapters,
        'chapter_data': chapters,
        'chapter_coverage': chapter_coverage
    }
    
    return coverage_data

def log_coverage_report(coverage_data):
    """Log a report of FLS coverage statistics"""
    logger.info("=== FLS Coverage Report ===")
    logger.info(f"Total FLS IDs: {coverage_data['total_ids']}")
    logger.info(f"Covered FLS IDs: {coverage_data['covered_ids']}")
    logger.info(f"Ignored FLS IDs: {coverage_data['ignored_ids']}")
    logger.info(f"Overall coverage: {coverage_data['overall_coverage']:.2f}%")
    
    logger.info("\nCoverage by chapter:")
    for chapter in coverage_data['chapters']:
        coverage = coverage_data['chapter_coverage'][chapter]
        if coverage == "IGNORED":
            logger.info(f"  Chapter {chapter}: IGNORED (all IDs are on ignore list)")
        else:
            logger.info(f"  Chapter {chapter}: {coverage:.2f}%")


    # def insert_fls_coverage(app, env, fls_ids):
    #     # here we should do the following:
    #     # * enrich the fls_ids with whether that FLS ID is covered by the coding guidelines
    #     pass
    # 
    # def calculate_fls_converage(fls_ids, fls_id_ignore_list):
    #     # note that fls_id_ignore_list should be a simple list of FLS IDs
    #     # * this should ideally be in its own .txt file with one line per FLS ID to ignore
    #     # * we should read this text file in up above in the check_fls function
    #     # here we should do the following:
    #     # * based on the fls_ids data structure, enriched by insert_fls_coverage, and the fls_id_ignore_list we should calculate
    #     #   * coverage percentage total over the entire FLS
    #     #   * coverage per chapter
    #     #     * if an entire chapter has all its FLS IDs on the ignore list, it should then just report an alternate thing,
    #     #       that cannot be confused for a number
    #     # * feel free to modify the fls_ids data structure to accomodate and make easier this processing
    #     pass


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
    check_fls_exists_and_valid_format(app, env)
    fls_ids = gather_fls_paragraph_ids(fls_url)
    logger.info(f"fls_ids:\n{fls_ids}")
    check_fls_ids_correct(app, env, fls_ids)

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


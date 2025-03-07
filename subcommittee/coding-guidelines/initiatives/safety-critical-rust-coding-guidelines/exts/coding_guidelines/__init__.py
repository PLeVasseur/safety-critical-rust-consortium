# SPDX-License-Identifier: MIT OR Apache-2.0
# SPDX-FileCopyrightText: The Coding Guidelines Subcommittee Contributors

import hashlib
import json
import re
import os
import tempfile

def source_transformer(app, docname, source):
    """Transform source to include options in need IDs"""
    # Create a debug log file in temp directory
    log_file = os.path.join(tempfile.gettempdir(), "sphinx_needs_debug.log")
    with open(log_file, "w") as f:
        f.write(f"Processing document: {docname}\n")
        f.write(f"Current directory: {os.getcwd()}\n\n")
    
    def log(msg):
        with open(log_file, "a") as f:
            f.write(f"{msg}\n")

    # Use a simpler approach: just find all directive lines and add IDs if missing
    lines = source[0].split('\n')
    modified_lines = []
    
    for i, line in enumerate(lines):
        # Check if this is a need directive
        need_match = re.match(r'(\s*)\.\.\s+(guideline|rationale|bad_example|good_example)::', line)
        if need_match:
            indent = need_match.group(1)
            need_type = need_match.group(2)
            log(f"Found {need_type} directive at line {i}: {line}")
            
            # Define prefixes
            prefix_map = {
                "guideline": "GUI_",
                "rationale": "RAT_", 
                "bad_example": "BAD_",
                "good_example": "GOOD_"
            }
            prefix = prefix_map.get(need_type, need_type[:3].upper() + "_")
            
            # Add the directive line
            modified_lines.append(line)
            
            # Check if the next line contains an ID
            has_id = False
            options = {}
            content = ""
            expected_indent = indent + "   "
            
            # Look ahead to see if there's an ID already
            j = i + 1
            while j < len(lines) and (lines[j].startswith(expected_indent) or not lines[j].strip()):
                if re.match(rf'{re.escape(expected_indent)}:id:', lines[j]):
                    has_id = True
                    log(f"  Already has ID: {lines[j]}")
                    break
                j += 1
            
            # If no ID found, extract content and options
            if not has_id:
                log("  No ID found, generating one...")
                
                # Extract options and content
                j = i + 1
                option_lines = []
                while j < len(lines):
                    if not lines[j].strip():
                        j += 1
                        continue
                        
                    if lines[j].startswith(expected_indent):
                        if ":" in lines[j]:
                            opt_match = re.match(rf'{re.escape(expected_indent)}:(\w+):\s*(.*)', lines[j])
                            if opt_match:
                                opt_name = opt_match.group(1)
                                opt_value = opt_match.group(2)
                                options[opt_name] = opt_value
                                log(f"  Found option: {opt_name}: {opt_value}")
                        else:
                            content += lines[j] + "\n"
                            log(f"  Found content: {lines[j]}")
                    else:
                        # End of this directive's options
                        break
                    j += 1
                
                # Generate hash-based ID
                hash_input = content + json.dumps(options, sort_keys=True)
                hash_obj = hashlib.sha1(hash_input.encode('UTF-8')).hexdigest().upper()
                need_id = f"{prefix}{hash_obj[:8]}"
                log(f"  Generated ID: {need_id}")
                
                # Insert the ID line right after the directive
                modified_lines.append(f"{expected_indent}:id: {need_id}")
            
        else:
            modified_lines.append(line)
    
    # Update the source
    source[0] = '\n'.join(modified_lines)
    
    # Log completion
    with open(log_file, "a") as f:
        f.write("\nTransformation complete\n")

def setup(app):
    app.connect('source-read', source_transformer)
    
    return {
        'version': '0.1',
        'parallel_read_safe': True,
    }

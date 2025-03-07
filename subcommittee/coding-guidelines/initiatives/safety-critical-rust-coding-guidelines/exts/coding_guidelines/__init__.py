# SPDX-License-Identifier: MIT OR Apache-2.0
# SPDX-FileCopyrightText: The Coding Guidelines Subcommittee Contributors

import hashlib
import json
import re

def source_transformer(app, docname, source):
    """Transform source to include options in need IDs"""
    lines = source[0].split('\n')
    new_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Detect need directives without IDs
        need_match = re.match(r'\.\. (guideline|rationale)::', line)
        if need_match:
            need_type = need_match.group(1)
            prefix = need_type[:3].upper() + "_"
            
            # Collect directive content
            directive_lines = [line]
            j = i + 1
            has_id = False
            options = {}
            content_lines = []
            
            # Process options and check for ID
            while j < len(lines) and (lines[j].startswith('   ') or not lines[j].strip()):
                if re.match(r'\s+:id:', lines[j]):
                    has_id = True
                elif re.match(r'\s+:(\w+):', lines[j]):
                    # Extract option name and value
                    opt_match = re.match(r'\s+:(\w+):\s*(.*)', lines[j])
                    if opt_match:
                        options[opt_match.group(1)] = opt_match.group(2)
                
                if not lines[j].strip():
                    # Parse content after blank line
                    k = j + 1
                    while k < len(lines) and (lines[k].startswith('   ') or not lines[k].strip()):
                        if lines[k].startswith('   '):
                            content_lines.append(lines[k].strip())
                        k += 1
                    break
                
                directive_lines.append(lines[j])
                j += 1
            
            # Generate hash ID if no ID exists
            if not has_id:
                # Combine content and options for hash
                content_str = '\n'.join(content_lines)
                hash_input = content_str
                if options:
                    hash_input += json.dumps(options, sort_keys=True)
                
                # Generate hash and ID
                hash_obj = hashlib.sha1(hash_input.encode('UTF-8')).hexdigest().upper()
                need_id = f"{prefix}{hash_obj[:8]}"
                
                # Insert ID after directive line
                directive_lines.insert(1, f"   :id: {need_id}")
            
            # Add the processed lines
            new_lines.extend(directive_lines)
            i = j
        else:
            new_lines.append(line)
            i += 1
    
    source[0] = '\n'.join(new_lines)

def setup(app):
    app.connect('source-read', source_transformer)
    
    return {
        'version': '0.1',
        'parallel_read_safe': True,
    }

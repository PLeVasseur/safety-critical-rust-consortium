# SPDX-License-Identifier: MIT OR Apache-2.0
# SPDX-FileCopyrightText: The Coding Guidelines Subcommittee Contributors

import hashlib
import json

def hash_based_id_function(env, needs_type, title, content, options):
    # Combine content and all options
    data_to_hash = content or ""
    
    # Add all options to the hash input
    if options:
        # Sort keys for consistent hash regardless of option order
        options_str = json.dumps(options, sort_keys=True)
        data_to_hash += options_str
    
    # Create hash
    hash_obj = hashlib.md5(data_to_hash.encode('utf-8'))
    hash_str = hash_obj.hexdigest()
    
    # You could use a prefix based on the need type
    prefix = needs_type[:3].upper()
    
    # Return ID with type prefix and first 8 chars of hash
    return f"{prefix}-{hash_str[:8]}"

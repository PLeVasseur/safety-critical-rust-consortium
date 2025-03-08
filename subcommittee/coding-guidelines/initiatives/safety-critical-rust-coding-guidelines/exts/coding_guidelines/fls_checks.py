# SPDX-License-Identifier: MIT OR Apache-2.0
# SPDX-FileCopyrightText: The Coding Guidelines Subcommittee Contributors

import requests
import logging
import re
from sphinx.errors import SphinxError
from sphinx_needs.data import SphinxNeedsData

# Get the Sphinx logger
logger = logging.getLogger('sphinx')

class FLSValidationError(SphinxError):
    category = "FLS Validation Error"

def check_fls(app, env):
    check_fls_exists_and_valid_format(app, env)
    check_fls_linkage_not_broken(app, env)

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

    
def check_fls_linkage_not_broken(app, env):
    pass

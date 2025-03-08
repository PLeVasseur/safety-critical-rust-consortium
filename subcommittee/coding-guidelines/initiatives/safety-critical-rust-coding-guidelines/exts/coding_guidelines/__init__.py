# SPDX-License-Identifier: MIT OR Apache-2.0
# SPDX-FileCopyrightText: The Coding Guidelines Subcommittee Contributors

from . import custom_need_id_hash
from . import fls_checks

from sphinx_needs.api import add_dynamic_function
from sphinx.errors import SphinxError

import logging

# Get the Sphinx logger
logger = logging.getLogger('sphinx')

def setup(app):
    
    app.connect('source-read', custom_need_id_hash.source_transformer)
    app.connect('env-check-consistency', fls_checks.check_fls)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
    }

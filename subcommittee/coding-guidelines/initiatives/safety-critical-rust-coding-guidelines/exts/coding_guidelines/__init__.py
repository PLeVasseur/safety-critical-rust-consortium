# SPDX-License-Identifier: MIT OR Apache-2.0
# SPDX-FileCopyrightText: The Coding Guidelines Subcommittee Contributors

from . import fls_checks
from . import write_guidelines_ids

from sphinx_needs.api import add_dynamic_function
from sphinx.errors import SphinxError

import logging

# Get the Sphinx logger
logger = logging.getLogger('sphinx')

def setup(app):
    
    app.connect('env-check-consistency', fls_checks.check_fls)
    app.connect('build-finished', write_guidelines_ids.build_finished)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
    }

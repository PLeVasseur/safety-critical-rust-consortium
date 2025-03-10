# SPDX-License-Identifier: MIT OR Apache-2.0
# SPDX-FileCopyrightText: The Coding Guidelines Subcommittee Contributors

from . import fls_checks
from . import write_guidelines_ids
from . import std_role

from sphinx_needs.api import add_dynamic_function
from sphinx.errors import SphinxError
from sphinx.domains import Domain

import logging

# Get the Sphinx logger
logger = logging.getLogger('sphinx')


class RustStdDomain(Domain):
    name = "coding-guidelines"
    label = "Rust Standard Library"
    roles = {
        "std": std_role.StdRefRole(),
    }
    directives = {}
    object_types = {}
    indices = {}
    
    def get_objects(self):
        return []
    
    def merge_domaindata(self, docnames, other):
        pass  # No domain data to merge

def setup(app):
    
    app.add_domain(RustStdDomain)
    app.add_config_value(
        name="spec_std_docs_url",
        default="https://doc.rust-lang.org/stable/std",
        rebuild="env",  # Rebuild the environment when this changes
        types=[str],
    )

    app.connect('env-check-consistency', fls_checks.check_fls)
    app.connect('build-finished', write_guidelines_ids.build_finished)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
    }

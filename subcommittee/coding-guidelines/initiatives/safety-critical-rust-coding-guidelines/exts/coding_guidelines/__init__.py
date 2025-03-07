# SPDX-License-Identifier: MIT OR Apache-2.0
# SPDX-FileCopyrightText: The Coding Guidelines Subcommittee Contributors

from . import custom_need_id_hash

def setup(app):
    app.connect('source-read', custom_need_id_hash.source_transformer)
    
    return {
        'version': '0.1',
        'parallel_read_safe': True,
    }

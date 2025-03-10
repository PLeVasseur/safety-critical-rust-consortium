#!/usr/bin/env -S uv run
# SPDX-License-Identifier: MIT OR Apache-2.0
# SPDX-FileCopyrightText: The Coding Guidelines Subcommittee Contributors

# Convenience script to generate a list of random paragraph IDs, ready to be
# copy-pasted as you write new paragraphs.

import string
import random

CHARS = string.ascii_letters + string.digits
LENGTH = 12
GENERATE = 10

for _ in range(GENERATE):
    id = "".join(random.choice(CHARS) for _ in range(LENGTH))
    print(f"   :id: gui_{id}")

    id = "".join(random.choice(CHARS) for _ in range(LENGTH))
    print(f"      :id: rat_{id}")

    id = "".join(random.choice(CHARS) for _ in range(LENGTH))
    print(f"      :id: bad_ex_{id}")

    id = "".join(random.choice(CHARS) for _ in range(LENGTH))
    print(f"      :id: good_ex_{id}")

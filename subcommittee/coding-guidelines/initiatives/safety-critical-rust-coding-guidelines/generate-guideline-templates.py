#!/usr/bin/env -S uv run
# SPDX-License-Identifier: MIT OR Apache-2.0
# SPDX-FileCopyrightText: The Coding Guidelines Subcommittee Contributors

import string
import random

# Configuration
CHARS = string.ascii_letters + string.digits
ID_LENGTH = 12
NUM_TEMPLATES = 5  # Default to generate one template, can be changed as needed

def generate_id(prefix):
    """Generate a random ID with the given prefix."""
    random_part = "".join(random.choice(CHARS) for _ in range(ID_LENGTH))
    return f"{prefix}_{random_part}"

def generate_guideline_template():
    """Generate a complete guideline template with all required sections."""
    # Generate IDs for all sections
    guideline_id = generate_id("gui")
    rationale_id = generate_id("rat")
    bad_example_id = generate_id("bad_ex")
    good_example_id = generate_id("good_ex")
    
    template = f""".. guideline:: Title Here
   :id: {guideline_id}
   :status: draft
   :fls: 
   :tags: 
   :category: 
   :recommendation: 

   Description of the guideline goes here.

   .. rationale:: 
      :id: {rationale_id}
      :status: draft

      Explanation of why this guideline is important.

   .. bad_example:: 
      :id: {bad_example_id}
      :status: draft
   
       .. code-block:: rust
   
         fn example_function() {{
             // Bad implementation
         }}

   .. good_example:: 
      :id: {good_example_id}
      :status: draft
   
       .. code-block:: rust
   
         fn example_function() {{
             // Good implementation
         }}
"""
    return template

def main():
    """Generate the specified number of guideline templates."""
    for i in range(NUM_TEMPLATES):
        if NUM_TEMPLATES > 1:
            print(f"=== Template {i+1} ===\n")
        
        template = generate_guideline_template()
        print(template)
        
        if NUM_TEMPLATES > 1 and i < NUM_TEMPLATES - 1:
            print("\n" + "=" * 80 + "\n")

if __name__ == "__main__":
    main()

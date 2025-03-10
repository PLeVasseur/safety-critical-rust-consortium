.. SPDX-License-Identifier: MIT OR Apache-2.0
   SPDX-FileCopyrightText: The Coding Guidelines Subcommittee Contributors

Generics
========

This section covers guidelines for function definitions and usage.

.. guideline:: Generics Guideline 1
   :id: gui_7zXCWxmZZ7ox
   :status: approved
   :fls: fls_sye3d17l9bf5
   :tags: readability
   :category: functions
   :recommendation: required

   Generics should...

   .. rationale:: 
      :id: rat_tXQ8NZqEm7JS
      :status: draft

      foo

   .. bad_example:: 
      :id: bad_ex_AWYJryOdAf42
      :status: approved
   
       .. code-block:: rust
   
         fn TotalPrice(items: &[Item]) -> f64 {
             // ...
             // Something about generics 1
         }

   .. good_example:: 
      :id: good_ex_VZT8SwBJV6Mm
      :status: approved

       .. code-block:: rust
   
         fn calculate_total_price(items: &[Item]) -> f64 {
             // ...
             // Something about generics 1
         }  


.. guideline:: Generics Guideline 2
   :id: gui_d4sQPPtjW4Mp
   :status: approved
   :fls: fls_lAdIRCFFlydD
   :tags: readability
   :category: functions
   :recommendation: encouraged

   Generics should...

   .. rationale:: 
      :id: rat_4vsva5oHv3TX
      :status: approved

      bar

   .. bad_example:: 
      :id: bad_ex_ilo9Zj3WjuXf
      :status: approved
   
       .. code-block:: rust
   
         fn TotalPrice(items: &[Item]) -> f64 {
             // ...
             // Something about generics 2
         }

   .. good_example:: 
      :id: good_ex_XNk5rXVnDfHc
      :status: approved

       .. code-block:: rust
   
         fn calculate_total_price(items: &[Item]) -> f64 {
             // ...
             // Something about generics 2
         }  


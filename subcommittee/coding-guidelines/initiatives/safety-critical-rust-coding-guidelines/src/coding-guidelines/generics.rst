.. SPDX-License-Identifier: MIT OR Apache-2.0
   SPDX-FileCopyrightText: The Coding Guidelines Subcommittee Contributors

Generics
========

This section covers guidelines for function definitions and usage.

.. guideline:: Generics Guideline 1
   :status: draft
   :fls: fls_sye3d17l9bf5
   :tags: readability
   :category: functions
   :recommendation: required

   Generics should...

   .. rationale:: 
      :status: draft

      foo

   .. bad_example:: 
      :status: approved
   
       .. code-block:: rust
   
         fn TotalPrice(items: &[Item]) -> f64 {
             // ...
             // Something about generics 1
         }

   .. good_example:: 
      :status: approved

       .. code-block:: rust
   
         fn calculate_total_price(items: &[Item]) -> f64 {
             // ...
             // Something about generics 1
         }  


.. guideline:: Generics Guideline 2
   :status: approved
   :fls: fls_sye3d17l9bf5
   :tags: readability
   :category: functions
   :recommendation: encouraged

   Generics should...

   .. rationale:: 
      :status: approved

      bar

   .. bad_example:: 
      :status: approved
   
       .. code-block:: rust
   
         fn TotalPrice(items: &[Item]) -> f64 {
             // ...
             // Something about generics 2
         }

   .. good_example:: 
      :status: approved

       .. code-block:: rust
   
         fn calculate_total_price(items: &[Item]) -> f64 {
             // ...
             // Something about generics 2
         }  


.. SPDX-License-Identifier: MIT OR Apache-2.0
   SPDX-FileCopyrightText: The Coding Guidelines Subcommittee Contributors

Functions
=========

This section covers guidelines for function definitions and usage.

.. guideline:: Function Naming Guideline
   :id: gui_ekiq2zlh1kG4
   :status: approved
   :fls: fls_sye3d17l9bf5
   :tags: readability
   :category: functions
   :recommendation: encouraged

   Functions should use lowercase snake_case for naming.

   .. rationale:: 
      :id: rat_nhjTBhhrMt2C
      :status: approved

      Consistent naming conventions improve code readability and maintainability. 
      Using verb phrases makes the purpose of functions immediately clear.

   .. bad_example:: 
      :id: bad_ex_ZWToGooHDw2e
      :status: approved
   
       .. code-block:: rust
   
         fn TotalPrice(items: &[Item]) -> f64 {
             // ...
             // other stuff related to function naming
         }

   .. good_example:: 
      :id: good_ex_DiHaxiq6SLOG
      :status: approved

       .. code-block:: rust
   
         fn calculate_total_price(items: &[Item]) -> f64 {
             // ...
             // other stuff related to function naming
         }  


.. guideline:: Some Other Function Guideline
   :id: gui_JIu2xC7UK9ie
   :status: draft
   :fls: fls_sye3d17l9bf5
   :tags: readability
   :category: functions
   :recommendation: encouraged

   Another kind of guideline

   .. rationale:: 
      :id: rat_101ggIrpH4dB
      :status: approved

      Other function guideline text

   .. bad_example:: 
      :id: bad_ex_FqOrS0eGg3BY
      :status: approved
   
       .. code-block:: rust
   
         fn TotalPrice(items: &[Item]) -> f64 {
             // ...
         }

   .. good_example:: 
      :id: good_ex_YFV1Vq8LMPGX
      :status: approved

       .. code-block:: rust
   
         fn calculate_total_price(items: &[Item]) -> f64 {
             // ...
         }  


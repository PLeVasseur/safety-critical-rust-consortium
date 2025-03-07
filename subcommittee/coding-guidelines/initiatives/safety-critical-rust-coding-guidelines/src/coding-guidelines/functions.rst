Functions
=========

This section covers guidelines for function definitions and usage.

.. guideline:: Function Naming Guideline
   :status: approved
   :tags: readability
   :category: functions
   :recommendation: encouraged

   Functions should use lowercase snake_case for naming.

   .. rationale:: 
      :status: approved

      Consistent naming conventions improve code readability and maintainability. 
      Using verb phrases makes the purpose of functions immediately clear.

   .. bad_example:: 
      :status: approved
   
       .. code-block:: rust
   
         fn TotalPrice(items: &[Item]) -> f64 {
             // ...
             // other stuff related to function naming
         }

   .. good_example:: 
      :status: approved

       .. code-block:: rust
   
         fn calculate_total_price(items: &[Item]) -> f64 {
             // ...
             // other stuff related to function naming
         }  


.. guideline:: Some Other Function Guideline
   :status: draft
   :tags: readability
   :category: functions
   :recommendation: encouraged

   Another kind of guideline

   .. rationale:: 
      :status: approved

      Other function guideline text

   .. bad_example:: 
      :status: approved
   
       .. code-block:: rust
   
         fn TotalPrice(items: &[Item]) -> f64 {
             // ...
         }

   .. good_example:: 
      :status: approved

       .. code-block:: rust
   
         fn calculate_total_price(items: &[Item]) -> f64 {
             // ...
         }  


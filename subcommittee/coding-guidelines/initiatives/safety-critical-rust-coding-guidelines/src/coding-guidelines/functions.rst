Functions
=========

This section covers guidelines for function definitions and usage.

.. guideline:: Function Naming
   :id: G_001
   :status: draft
   :tags: readability
   :category: functions
   :recommendation: encouraged

   Functions should use lowercase snake_case for naming.

   .. rationale:: -
      :id: RAT_001

      Consistent naming conventions improve code readability and maintainability. 
      Using verb phrases makes the purpose of functions immediately clear.

   .. bad_example:: -
      :id: BAD_EX_001
      :status: draft
   
       .. code-block:: rust
   
         fn TotalPrice(items: &[Item]) -> f64 {
             // ...
         }

   .. good_example:: -
      :id: GOOD_EX_001
      :status: draft

       .. code-block:: rust
   
         fn calculate_total_price(items: &[Item]) -> f64 {
             // ...
         }  


.. guideline:: Function Naming
   :id: G_002
   :status: draft
   :tags: readability
   :category: functions
   :recommendation: encouraged

   Functions should use lowercase snake_case for naming.

   .. rationale:: -
      :id: RAT_002
      :status: draft

      Consistent naming conventions improve code readability and maintainability. 
      Using verb phrases makes the purpose of functions immediately clear.

   .. bad_example:: -
      :id: BAD_EX_002
      :status: draft
   
       .. code-block:: rust
   
         fn TotalPrice(items: &[Item]) -> f64 {
             // ...
         }

   .. good_example:: -
      :id: GOOD_EX_002
      :status: draft

       .. code-block:: rust
   
         fn calculate_total_price(items: &[Item]) -> f64 {
             // ...
         }  

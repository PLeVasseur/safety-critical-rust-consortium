Generics
========

This section covers guidelines for function definitions and usage.

.. guideline:: Generics Guideline 1
   :id: G_GENERICS_001
   :status: draft
   :tags: readability
   :category: functions
   :recommendation: encouraged

   Generics should...

   .. rationale:: -
      :id: RAT_GENERICS_001
      :status: draft

      Consistent naming conventions improve code readability and maintainability. 
      Using verb phrases makes the purpose of functions immediately clear.

   .. bad_example:: -
      :id: BAD_EX_GENERICS_001
      :status: draft
   
       .. code-block:: rust
   
         fn TotalPrice(items: &[Item]) -> f64 {
             // ...
         }

   .. good_example:: -
      :id: GOOD_EX_GENERICS_001
      :status: draft

       .. code-block:: rust
   
         fn calculate_total_price(items: &[Item]) -> f64 {
             // ...
         }  


.. guideline:: Generics Guideline 2
   :id: G_GENERICS_002
   :status: draft
   :tags: readability
   :category: functions
   :recommendation: encouraged

   Generics should...

   .. rationale:: -
      :id: RAT_GENERICS_002
      :status: draft

      Consistent naming conventions improve code readability and maintainability. 
      Using verb phrases makes the purpose of functions immediately clear.

   .. bad_example:: -
      :id: BAD_EX_GENERICS_002
      :status: draft
   
       .. code-block:: rust
   
         fn TotalPrice(items: &[Item]) -> f64 {
             // ...
         }

   .. good_example:: -
      :id: GOOD_EX_GENERICS_002
      :status: draft

       .. code-block:: rust
   
         fn calculate_total_price(items: &[Item]) -> f64 {
             // ...
         }  


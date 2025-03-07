Generics
========

This section covers guidelines for function definitions and usage.

.. guideline:: Generics Guideline 1
   :status: draft
   :tags: readability
   :category: functions
   :recommendation: required

   Generics should...

   .. rationale:: 
      :status: draft

      foo

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
   :status: draft
   :tags: readability
   :category: functions
   :recommendation: encouraged

   Generics should...

   .. rationale:: 
      :status: draft

      bar

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


Functions
=========

This section covers guidelines for function definitions and usage.

.. guideline:: Function Naming
   :id: FUNC_001
   :status: draft
   :tags: readability
   :category: functions
   :recommendation: encouraged

   Functions should use lowercase snake_case for naming.

.. rationale:: Function Naming Rationale
   :id: RAT_FUNC_001
   :status: draft
   :tags: readability
   :links: FUNC_001

   Consistent naming conventions improve code readability and maintainability.
   Using verb phrases makes the purpose of functions immediately clear.

.. example:: Function Naming Examples
   :id: EX_FUNC_001
   :status: draft
   :tags: readability
   :links: FUNC_001

   **Good example:**
   
   .. code-block:: rust
   
      fn calculate_total_price(items: &[Item]) -> f64 {
          // ...
      }
   
   **Bad example:**
   
   .. code-block:: rust
   
      fn TotalPrice(items: &[Item]) -> f64 {
          // ...
      }

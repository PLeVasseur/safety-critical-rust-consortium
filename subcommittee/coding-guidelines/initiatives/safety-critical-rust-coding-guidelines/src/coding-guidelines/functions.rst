Functions
=========

This section covers guidelines for function definitions and usage.

.. guideline:: Function Naming
   :id: FUNC_001
   :status: approved
   :tags: readability
   :severity: medium
   :category: naming

   Functions should use lowercase snake_case for naming.

   .. recommendation::
      :id: REC-FUNC-001

      Function names should be verb phrases that clearly describe what the function does.

   .. rationale::
      :id: RAT-FUNC-001

      Consistent naming conventions improve code readability and maintainability.
      Using verb phrases makes the purpose of functions immediately clear.

   .. code-block:: rust

      // Good
      fn calculate_total_price(items: &[Item]) -> f64 {
          // ...
      }

      // Bad
      fn TotalPrice(items: &[Item]) -> f64 {
          // ...
      }

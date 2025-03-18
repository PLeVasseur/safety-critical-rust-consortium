.. SPDX-License-Identifier: MIT OR Apache-2.0
   SPDX-FileCopyrightText: The Coding Guidelines Subcommittee Contributors

.. default-domain:: coding-guidelines

Inline Assembly
===============

This document provides guidelines for using inline assembly in Rust code...

.. guideline:: All usage of inline assembly must be thoroughly documented   
   :id: gui_vZE9kLPQ7m93
   :status: draft
   :fls: fls_z1il3w9nulzy
   :tags: security, reduce-human-error, readability 
   :category: 
   :recommendation: required 

   .. note::
      **MISRA Reference** 
      All usage of assembly code must be documented, including the purpose, inputs, outputs, side effects, and safety considerations.

   .. rationale:: 
      :id: rat_Rb0kktvGhbVk
      :status: draft

      Inline assembly can introduce undefined behavior if not properly documented.  
      - If the assembly fails to execute correctly, the return value may be uninitialized, leading to unpredictable results.
      - Functions that assume success without error handling can cause silent failures in production.
      - Without clear comments, maintainers may misuse the function, leading to integration errors or security issues.

   .. bad_example:: 
      :id: bad_ex_V1rThIfyrmTQ
      :status: draft

      The following code is **non-compliant** with THE guidelines because:
      - It does not specify `nomem` and `nostack` constraints.
      - The return value `result` might be uninitialized if the inline assembly fails.
      - It lacks documentation, making it hard to maintain.

      .. code-block:: rust

         pub fn bad_add_asm(a: u32, b: u32) -> u32 {
             let result: u32;
             unsafe {
                 asm!(
                     "add {0}, {1}, {2}",
                     out(reg) result,
                     in(reg) a,
                     in(reg) b
                 );
             }
             result // Possible UB: result might be uninitialized if asm fails
         }

   .. good_example:: 
      :id: good_ex_tDWewxl8qUE4
      :status: draft

      .. note::
         The following example adheres to THE guidelines by ensuring:
         - The use of `options(nomem, nostack)` to prevent unexpected memory modifications.
         - Proper inline documentation to describe inputs, outputs, and safety considerations.

      .. code-block:: rust

         /// # Safe Inline Assembly Addition
         ///
         /// This function takes two `u32` values and returns their sum using inline assembly.
         /// - Adheres to Rust guidelines (structured, documented, and avoids undefined behavior).
         /// - Uses explicit register constraints to prevent side effects.
         ///
         /// ## Safety Considerations:
         /// - Inline assembly is carefully constrained to avoid modifying unintended registers.
         /// - No undefined behavior (e.g., no division by zero, out-of-range values).
         ///
         /// # Arguments:
         /// - `a`: First operand.
         /// - `b`: Second operand.
         ///
         /// # Returns:
         /// - Sum of `a` and `b` (`u32`).
         ///
         /// # Example:
         /// ```
         /// let result = add_asm(2, 3);
         /// assert_eq!(result, 5);
         /// ```
         #[inline(always)]
         pub fn add_asm(a: u32, b: u32) -> u32 {
             let result: u32;
             unsafe {
                 asm!(
                     "add {0}, {1}, {2}", // ARM syntax: add result, a, b
                     out(reg) result,     // Output operand
                     in(reg) a,           // Input operand a
                     in(reg) b,           // Input operand b
                     options(nomem, nostack) // Ensures no memory or stack modifications
                 );
             }
             result
         }

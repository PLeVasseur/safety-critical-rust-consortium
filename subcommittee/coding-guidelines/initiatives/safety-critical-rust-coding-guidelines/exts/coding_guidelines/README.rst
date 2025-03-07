.. SPDX-License-Identifier: MIT OR Apache-2.0
   SPDX-FileCopyrightText: The Coding Guidelines Subcommittee Contributors

==================================
Coding Guidelines Sphinx Extension
==================================

To enhance the Safety-Critical Rust Coding Guidelines, and to facilitate its
authoring, updating, and testing it easier, we developed and use a custom
Sphinx extension that adds new roles and directives. The source code of the
extension is in the ``exts/coding_guidelines`` directory.

.. contents:: In this document:

Needs IDs Generated From Content and Options
============================================

We generate unique IDs per ``guideline``, ``rationale``, ``bad_example``, and
``good_example`` based on:

* content
* all options

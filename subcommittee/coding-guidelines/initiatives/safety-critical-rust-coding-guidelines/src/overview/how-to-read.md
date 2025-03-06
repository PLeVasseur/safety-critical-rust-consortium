# How to Read

## Coding Guideline Format

These are the categories contained in each coding guideline. Their definition must be precise in order to generate a machine-parseable representation.

### Title

The title of the coding guideline. Includes a specifier to identify each coding guideline uniquely.

#### Format

**Must** be of the form `Rule <corresponding section of Ferrocene Language Specification>.<Latin alphabet signifier A-Z, AA-AZ, AAZ - AAZ, and so on>: <plain text description of rule>` on its own line. Note that we choose to use `<Latin alphabet signifier>` to disambiguate with the particular section we're covering of the Ferrocene Language Specification.

Examples:

> Rule 4.3.3.2.A: Avoid implicit wrapping behavior in integer math 
> Rule 4.3.3.2.B: Avoid implicit casts between integer types
> ...
> Rule 4.3.3.2.Z: Yet another rule
> Rule 4.3.3.2.AA: Yet one more rule

**Must not** have duplicate specifier, where specifier is defined as the `<corresponding section of Ferrocene Language Specification>.<Latin alphabet signifier A-Z, AA-AZ, AAZ - AAZ, and so on>`.

**Must** be its own section, thus in plaintext it will have one or more leading `#`, followed by a space, followed by the rule.

### Recommendation

Possible values are:

* Required
* Encouraged

#### Format

**Must** be of the form `Recommendation: <recommendation-category>` on its own line.

### Automation

Possible values are:

* Possible
* Impossible

#### Format

**Must** be of the form `Automation: <automation-category>` on its own line.

There need not currently be automated tooling to perform this check in existence. "Possible" here means that we believe that determining this property should be possible with automated tooling.

### Rationale:

A block of text describing the rationale for the existence of this coding guideline.

#### Format

**Must not** include any additional Markdown sections, i.e. no usage of `#` within this block.

**May** use various types of Markdown formatting such as **bold** and _italics_.

### Negative Example

A negative example, showcasing how if this coding guideline is not used some potential error or unintended consequence can occur.

#### Format

**Must** have `**Negative Example**` on it own line.

**Must** have one or more pieces of prose to set the stage for understanding the code example following `**Negative Example**`.

Explanation of code example **may** include one or more paragraphs.

**Must** have a short code example following the explanation of the format:

```rust
<example code goes here>
```

**Must** have comments within code example to explain issue.

**Strive** to keep code example to within 5 - 10 lines to aid in understanding.

### Positive Example


A positive example, showcasing how if this coding guideline is used we can prevent potential errors or unintended consequences.

#### Format

**Must** have `**Positive Example**` on it own line.

**Must** have one or more pieces of prose to set the stage for understanding the code example following `**Positive Example**`.

Explanation of code example **may** include one or more paragraphs.

**Must** have a short code example following the explanation of the format:

```rust
<example code goes here>
```

**Must** have comments within code example to explain issue.

**Strive** to keep code example to within 5 - 10 lines to aid in understanding.

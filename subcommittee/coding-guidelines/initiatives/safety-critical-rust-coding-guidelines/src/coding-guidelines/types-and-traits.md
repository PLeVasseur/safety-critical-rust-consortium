# 4. Types and Traits

## 4.1 Types

## 4.2 Type Classification

## 4.3 Scalar Types

### 4.3.3 Numeric Types

#### 4.3.3.2 Integer Types

##### Rule 4.3.3.2.A: Avoid implicit wrapping behavior in integer math

Category: Encouraged

Automation: Possible

Rationale:

In Rust, handling of integer overflow and underflow does differ between debug and release builds, which is an important consideration for safety-critical systems.

**Debug vs. Release Behavior**

Debug builds: Rust performs overflow checking and will panic (crash) when an overflow/underflow occurs. This helps catch potential issues during development.

Release builds: By default, Rust performs "wrapping" behavior where values silently wrap around their bounds (similar to C/C++).

While not crashing is an important quality of a safety-critical system, implicit wrapping behavior which is unaccounted for can also cause harm depending on context.

**Be Explicit in Usage**

We encourage usage of explicit operations on integers from `core` for clarity at point of usage. For example, the range of options include but are not limited to:

* [checked_add()](https://doc.rust-lang.org/std/primitive.u32.html#method.checked_add)
* [overflowing_add()](https://doc.rust-lang.org/std/primitive.u32.html#method.overflowing_add)
* [saturating_add()](https://doc.rust-lang.org/std/primitive.u32.html#method.saturating_add)
* [unchecked_add()](https://doc.rust-lang.org/std/primitive.u32.html#method.unchecked_add)
* [wrapping_add()](https://doc.rust-lang.org/std/primitive.u32.html#method.wrapping_add)

Various arithmetic operations are covered including addition, subtraction, multiplication, and division.

**Negative Example**

Imagine we calculate a buffer size to later use when allocating a container. If we use the `Mul` operation we may have an implicit wrap, causing us to under-allocate the container.

```rust
fn calculate_buffer_size(num_elements: u32, element_size: u32) -> u32 {
    // Dangerous: Can silently overflow in release builds
    let buffer_size = num_elements * element_size;
    
    // Allocate buffer with potentially incorrect size
    buffer_size
}
```

**Positive Example**

If instead we use the `checked_mul()` function, we can ensure that we either arrive within the bounds of the integer type or do not perform the operation and return `None`. Knowledge about whether the operation succeeded or not can determine next steps to take.

```rust
fn calculate_buffer_size_checked(num_elements: u32, element_size: u32) -> Result<u32, &'static str> {
    // Use checked_mul to explicitly handle potential overflow
    match num_elements.checked_mul(element_size) {
        Some(buffer_size) => Ok(buffer_size),
        None => Err("Buffer size calculation would overflow")
    }
}
```

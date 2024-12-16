Implementation of Dual Numbers and Operations
=============================================

.. contents:: Table of Contents
   :local:

Overview of the Dual Class
--------------------------

The `dual.py` file implements the `Dual` class, the core of the `dual_autodiff` package. This class defines dual numbers and supports operations such as addition, subtraction, multiplication, and division.

### Arithmetic Operations
The `Dual` class overrides arithmetic operators for seamless integration. For example::

    x = Dual(2, 1)
    y = Dual(3, 2)
    print(x + y)  # Output: Dual(real=5, dual=3)

### Mathematical Functions
The `Dual` class also implements key mathematical functions such as:

- Trigonometric functions (`sin`, `cos`, `tan`).
- Exponential and logarithmic functions (`exp`, `log`).
- Hyperbolic functions (`sinh`, `cosh`, `tanh`).
- Square root (`sqrt`).

For example::

    x = Dual(2, 1)
    result = x.sin()
    print(result)  # Output: Dual(real=0.9092..., dual=-0.4161...)

### Error Handling and Special Cases
The `Dual` class ensures that mathematical operations like `log` and `sqrt` are only applied within valid domains, raising appropriate errors when encountering invalid inputs.

### Example of Using Dual Numbers
Consider the function:

.. math::

   f(x) = \log(x) + x^2 \implies f'(x) = \frac{1}{x} + 2x.

This can be evaluated directly using the `Dual` class::

    x = Dual(2, 1)
    f_x = x.log() + x**2  # Output: Dual(real=4.0, dual=4.5)

Utility Functions
-----------------
To enhance usability and simplify mathematical operations, two utility modules are provided as part of the package:

- **`functions.py`:** Provides global aliases for commonly used mathematical functions, such as `sin`, `cos`, `log`, and `sqrt`. These aliases act as wrappers around the corresponding methods of the `Dual` class, allowing users to apply these functions directly to `Dual` instances or standard numerical values. For example::

      from dual_autodiff.functions import sin, cos, log
      x = Dual(2, 1)
      result = sin(x) + log(x)

- **`base.py`:** Includes helper functions:
  - `is_dual_instance(value)`: Checks whether a given value is an instance of the `Dual` class.
  - `ensure_dual(value)`: Wraps a non-`Dual` value into a `Dual` object with its derivative initialized to zero.

These utility functions make the library more accessible for a wide range of users.


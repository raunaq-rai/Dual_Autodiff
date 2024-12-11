# rsr45-dual-autodiff-x

`rsr45-dual-autodiff-x` is a Python package that provides an efficient and user-friendly implementation of dual numbers for automatic differentiation. This package is optimized using Cython for improved performance.

---

## Features

- **Dual Number Arithmetic**: Supports basic operations like addition, subtraction, multiplication, and division.
- **Mathematical Functions**: Includes trigonometric, exponential, logarithmic, and other common mathematical functions.
- **Automatic Differentiation**: Computes derivatives automatically as a natural part of the computation.
- **Cython Optimization**: Improved performance for computationally intensive tasks.

---

## Installation

### Using pip
Install the package directly from PyPI:

```bash
pip install rsr45-dual-autodiff-x
```

### Using github
 1. Clone the repository
 ```bash
 git clone https://gitlab.developers.cam.ac.uk/phy/data-intensive-science-mphil/assessments/c1_coursework1/rsr45.git
 ```

 2. Navigate to dual_autodiff_x
 ```bash
 cd dual_autodiff_x
 ```

 3. Install the package
 ```bash
 pip install e .
 ```

## Usage

### Importing the Package

```python
import dual_autodiff_x as df_x
from dual_autodiff_x.dual import Dual as DualOptimized
from dual_autodiff_x.functions import sin as sin_optimized, cos as cos_optimized, log as log_optimized
```

### Using `dual_autodiff_x` (Optimized Version)
```python
x_optimized = DualOptimized(2, 1)  # Represents the dual number 2 + 1ε
```

---

## Performing Operations

### Using dual_autodiff_x (Optimized Version)

```python
# Example: f(x) = log(sin(x)) + x^2 * cos(x)
f_x_optimized = log_optimized(sin_optimized(x_optimized)) + x_optimized**2 * cos_optimized(x_optimized)
print(f_x_optimized)  # Output the result and its derivative
```

---

## Why Use dual_autodiff_x?

The `rsr-dual-autodiff-x` package is an optimized version of `dual_autodiff`, built with Cython for better performance. Use it when speed is a priority, especially for computationally intensive tasks.

---

## Licence

This project is licensed under the MIT License.

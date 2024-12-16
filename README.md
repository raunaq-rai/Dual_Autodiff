# dual_autodiff

`dual_autodiff` is a Python package for automatic differentiation using dual numbers. It simplifies derivative computations for mathematical functions and operations. Additionally, the package includes a Cython-optimized version, `dual_autodiff_x`, for enhanced performance.

---

## Features

- **Dual Numbers**: Efficient representation of derivatives alongside function values.
- **Rich Mathematical Functions**: Includes trigonometric, logarithmic, exponential, and hyperbolic functions.
- **Arithmetic Operations**: Supports addition, subtraction, multiplication, division, and power operations.
- **Cython Optimization**: Enhanced performance through compiled Cython code in `dual_autodiff_x`.

---

## Installation

### Prerequisites
- Python 3.9 or higher.
- `pip` for package installation.
- `conda` (optional) for managing virtual environments.

### Installing `dual_autodiff`

#### Using `pip`
Install the package directly from PyPI:
```bash
pip install rsr45-dual-autodiff
pip install numpy
pip install pytest
```

Or Clone the repository and install the package:

```bash
git clone 'https://gitlab.developers.cam.ac.uk/phy/data-intensive-science-mphil/assessments/c1_coursework1/rsr45.git'
cd dual_autodiff
pip install e .
pip install -r requirements.txt
```

#### Using conda
1. Create a virtual environment using the provided `environment.yaml` file:
```bash
conda env create -n dual_env -f environment.yaml
```
2. Activate the environment:
```bash
conda activate dual_env
```
3. Install the package within this environment:
```bash
pip install -e .
pip install -r requirements.txt
```

---

## How It Works

### Dual Numbers and Automatic Differentiation

Dual numbers are a mathematical construct that extend real numbers to encode both a function's value and its derivative in a single representation. They are written as:

\[
a + b $\epsilon$
\]

Where:
- a is the **real part**, representing the value of the function.
- b is the **dual part**, representing the derivative of the function.
- $\epsilon$ is an infinitesimal unit such that \($\epsilon$^2 = 0\), meaning any higher powers of \($\epsilon$) vanish.

### Application in Automatic Differentiation

Dual numbers are at the core of **forward-mode automatic differentiation**, a technique used to compute derivatives efficiently and exactly. By propagating dual numbers through a computation, both the function value and its derivative are calculated simultaneously.

#### Key Idea:
For any differentiable function \(f(x)\), dual numbers allow the computation of derivatives as:
\[
f(a + b $\epsilon$) = f(a) + f'(a)b $\epsilon$
\]
Where:
- \(f(a)\) is the function value.
- \(f'(a)b\) is the derivative scaled by \(b\).

This property eliminates the need for symbolic differentiation or numerical approximation (e.g., finite differences), making it both accurate and computationally efficient.


---

## Usage
### Using `dual_autodiff`

See `dual_autodiff.ipynb` within docs for examples

```python
from dual_autodiff import Dual, sin, cos

# Create a Dual object
x = Dual(1.0, 1.0)  

# Perform operations
y = sin(x)
print(f"Value: {y.real}, Derivative: {y.dual}")
```

## Available Functions

### **Dual Class Methods**

The `Dual` class provides a range of methods for performing arithmetic operations, trigonometric functions, exponential/logarithmic calculations, and hyperbolic functions, along with automatic differentiation.

---

#### **Arithmetic Operations**
- `__add__`, `__radd__`: Addition.
- `__sub__`, `__rsub__`: Subtraction.
- `__mul__`, `__rmul__`: Multiplication.
- `__truediv__`, `__rtruediv__`: Division.
- `__pow__`: Power.

---

#### **Trigonometric Functions**
- `sin()`: Computes the sine of the dual number.
- `cos()`: Computes the cosine of the dual number.
- `tan()`: Computes the tangent of the dual number.
- `asin()`: Computes the arcsine of the dual number (`-1 <= x <= 1`).
- `acos()`: Computes the arccosine of the dual number (`-1 <= x <= 1`).
- `atan()`: Computes the arctangent of the dual number.

---

#### **Exponential and Logarithmic Functions**
- `exp()`: Computes the exponential (e^x) of the dual number.
- `log()`: Computes the natural logarithm of the dual number (`x > 0`).
- `sqrt()`: Computes the square root of the dual number (`x >= 0`).

---

#### **Hyperbolic Functions**
- `sinh()`: Computes the hyperbolic sine of the dual number.
- `cosh()`: Computes the hyperbolic cosine of the dual number.
- `tanh()`: Computes the hyperbolic tangent of the dual number.

---

### **Example Usage**

```python
from dual_autodiff import Dual

# Create Dual numbers
x = Dual(2.0, 1.0)  # Real part = 2.0, Dual part = 1.0
y = Dual(3.0, 2.0)  # Real part = 3.0, Dual part = 2.0

# Arithmetic Operations
print(f"Addition: {x} + {y} = {x + y}")         # 5 + 3ε
print(f"Subtraction: {x} - {y} = {x - y}")      # -1 - 1ε
print(f"Multiplication: {x} * {y} = {x * y}")   # 6 + 7ε
print(f"Division: {x} / {y} = {x / y}")         # 2/3 - 1/3ε
print(f"Power: {x}^2 = {x ** 2}")               # 4 + 4ε

# Trigonometric Functions
print(f"Sine: sin({x}) = {x.sin()}")            # sin(2) + cos(2)ε
print(f"Cosine: cos({x}) = {x.cos()}")          # cos(2) - sin(2)ε
print(f"Tangent: tan({x}) = {x.tan()}")         # tan(2) + sec^2(2)ε

# Exponential and Logarithmic Functions
print(f"Exponential: exp({x}) = {x.exp()}")     # e^2 + e^2ε
print(f"Logarithm: log({x}) = {x.log()}")       # log(2) + 1/2ε
print(f"Square Root: sqrt({x}) = {x.sqrt()}")   # sqrt(2) + 1/(2sqrt(2))ε

# Hyperbolic Functions
print(f"Hyperbolic Sine: sinh({x}) = {x.sinh()}")  # sinh(2) + cosh(2)ε
print(f"Hyperbolic Cosine: cosh({x}) = {x.cosh()}")  # cosh(2) + sinh(2)ε
print(f"Hyperbolic Tangent: tanh({x}) = {x.tanh()}")  # tanh(2) + sech^2(2)ε
```
---

### **Global Functions in `functions.py`**

These functions are global aliases for the corresponding `Dual` class methods, allowing them to be called directly with either `float` or `Dual` inputs. The use of these aliases simplifies the syntax when working with `Dual` objects and standard numeric values.

#### **Available Functions**

##### **Trigonometric Functions**
- `sin(x)`: Computes the sine of `x`.
- `cos(x)`: Computes the cosine of `x`.
- `tan(x)`: Computes the tangent of `x`.
- `asin(x)`: Computes the arcsine of `x` (only for `-1 <= x <= 1`).
- `acos(x)`: Computes the arccosine of `x` (only for `-1 <= x <= 1`).
- `atan(x)`: Computes the arctangent of `x`.

##### **Exponential and Logarithmic Functions**
- `exp(x)`: Computes the exponential of `x` (e^x).
- `log(x)`: Computes the natural logarithm of `x` (only for `x > 0`).
- `sqrt(x)`: Computes the square root of `x` (only for `x >= 0`).

##### **Hyperbolic Functions**
- `sinh(x)`: Computes the hyperbolic sine of `x`.
- `cosh(x)`: Computes the hyperbolic cosine of `x`.
- `tanh(x)`: Computes the hyperbolic tangent of `x`.

---

### **How to Use `functions.py`**

The functions provided in `functions.py` can be used directly for both numeric (`float`) and dual (`Dual`) inputs. This allows seamless integration of dual numbers with standard numerical operations.

#### **Example Usage**
```python
from dual_autodiff import sin, cos, log, Dual

# Using Dual numbers
x_dual = Dual(1.0, 1.0)  # Real part = 1.0, Dual part = 1.0
result_dual = sin(x_dual) + log(x_dual)
print(f"Result with Dual input: {result_dual.real}, Derivative: {result_dual.dual}")
```

---

### Cython Optimization

The `dual_autodiff_x` package uses Cython to compile critical operations into C, providing a significant speed boost for computationally intensive tasks.
See `dual_autodiff_x` README.md for further information





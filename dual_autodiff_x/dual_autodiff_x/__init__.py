from .dual import Dual
from .functions import (
    sin, cos, tan, log, exp, sqrt,
    sinh, cosh, tanh, asin, acos, atan
)

# Define the version directly here
__version__ = "0.1.13"

# Define the public API
__all__ = [
    "__version__",  # Expose version information
    "Dual",         # Expose the Dual class
    "sin", "cos", "tan", "log", "exp", "sqrt",  # Expose functions
    "sinh", "cosh", "tanh", "asin", "acos", "atan"
]


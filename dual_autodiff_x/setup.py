from setuptools import setup, Extension, find_packages
from Cython.Build import cythonize

# Define Cython extensions, linking to the C source files
extensions = [
    Extension("dual_autodiff.dual", ["dual_autodiff/dual.c"]),
    Extension("dual_autodiff.functions", ["dual_autodiff/functions.c"]),
    Extension("dual_autodiff.version", ["dual_autodiff/version.c"]),
]

# Setup configuration
setup(
    name="dual_autodiff_x",
    version="0.1.0",
    author="Raunaq Rai",
    description="A package for automatic differentiation using dual numbers.",
    packages=find_packages(exclude=["tests*", "docs*", "*.pyx"]),  # Exclude `.pyx` files
    ext_modules=cythonize(
        extensions,
        compiler_directives={"language_level": "3"},  # Python 3 language level
    ),
    zip_safe=False,  # Required for extensions
    include_package_data=True,  # Include additional non-Python files
)


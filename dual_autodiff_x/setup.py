from setuptools import setup, Extension
from Cython.Build import cythonize

# Cythonize your modules
cython_modules = [
    Extension("dual_autodiff.dual", ["dual_autodiff/dual.py"]),
    Extension("dual_autodiff.functions", ["dual_autodiff/functions.py"]),
    Extension("dual_autodiff.version", ["dual_autodiff/version.py"]),
]

setup(
    name="dual_autodiff_x",
    version="0.1.0",
    author="Raunaq Rai",
    packages=["dual_autodiff"],
    ext_modules=cythonize(
        cython_modules,
        compiler_directives={"language_level": "3"}  # Python 3 compatibility
    ),
    zip_safe=False,
)


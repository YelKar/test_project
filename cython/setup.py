from Cython.Distutils import build_ext
from setuptools import setup
from distutils.extension import Extension


sources = ["main.pyx"]
ext_modules = [
    Extension(
        "main",
        sources
    ),
]

setup(
    name="main",
    cmdclass={"build_ext": build_ext},
    ext_modules=ext_modules,
)

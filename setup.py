from pathlib import Path
from setuptools import setup, glob
from pybind11.setup_helpers import Pybind11Extension, build_ext


__version__ = "1.0.0"

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")


ext_modules = [
    Pybind11Extension(
        "whr_core",
        glob.glob("src/*.cc"),
        define_macros=[("VERSION_INFO", __version__)],
    ),
]

setup(
    name="whr_chess",
    packages=["whr_chess"],
    version=__version__,
    license="MIT",
    author="Viet-Anh Tran",
    url="https://github.com/CallOn84/whole_history_rating/",
    download_url=f"https://github.com/CallOn84/whole_history_rating/archive/{__version__}.tar.gz",
    description="An adaptation of wind23's whole_history_rating for chess",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["WHR", "whole history rating", "Elo rating"],
    ext_modules=ext_modules,
    extras_require={"test": "pytest"},
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)

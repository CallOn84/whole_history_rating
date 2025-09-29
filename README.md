Whole History Rating for Chess
====================

## Description

This is an adaptation of wind23's whole_history_rating repository for chess.

The original implementation is based on the [Ruby code](https://github.com/goshrine/whole_history_rating) of [GoShrine](http://goshrine.com).

## Installation

To install it from PyPI:

    pip install whr

To install it from source code:

    git clone git@github.com:CallOn84/whole_history_rating.git
    pip install ./whole_history_rating

To build this package from the source code, you will need a recent version of Python 3 installed, along with `setuptools>=42` and `pybind11>=2.10.0`. Furthermore, depending on your operating system, you may also require the installation of the appropriate C++ build environment. If you are uncertain about the required dependencies, you can begin by attempting `pip install` and follow the instructions provided by your system to install the necessary components.

## References

Rémi Coulom. [Whole-history rating: A Bayesian rating system for players of time-varying strength](https://www.remi-coulom.fr/WHR/WHR.pdf). In _International Conference on Computers and Games_. 2008.

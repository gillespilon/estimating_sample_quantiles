<!--
[![Coverity Scan Build Status](https://img.shields.io/coverity/scan/10257.svg)](https://scan.coverity.com/projects/gillespilon-estimating_sample_quantiles)
[![Travis](https://img.shields.io/travis/rust-lang/rust.svg)](https://travis-ci.org/gillespilon/estimating_sample_quantiles)
-->

# In brevi

The purpose of this repository is to illustrate the many methods to estimate sample quantiles. This arose while comparing results from NumPy with Minitab statistical software, which led to questions of why the difference. This is important to me because the differences in Q1 and Q3 lead to practically significant differences in estimates of the confidence intervals of Q2.

I use functions from NumPy and SciPy to estimate quantiles. I might have to code my own functions for the other methods for which functions do not exist.

# Methodology

The various algorithms for estimating quantiles are described in the notebook as well as the documentation within the NumPy and SciPy functions.

# References

[numpy.quantile](https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.quantile.html?highlight=quantile)

[scipy.stats.mstats.mquantiles](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mstats.mquantiles.html)

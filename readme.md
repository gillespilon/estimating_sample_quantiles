[![Coverity Scan Build Status](https://img.shields.io/coverity/scan/10257.svg)](https://scan.coverity.com/projects/gillespilon-estimating_sample_quantiles)
[![Travis](https://img.shields.io/travis/rust-lang/rust.svg)](https://travis-ci.org/gillespilon/estimating_sample_quantiles)

# In brevi

The purpose of this repository is to estimate quantiles using various methods. This arose while comparing results from numpy with Minitab statistical software, which led to questions of why the difference. This is important to me because the differences in Q1 and Q3 lead to practically significant differences in estimates of the confidence intervals of Q2.

I use functions from numpy and scipy to estimate quantiles. I might have to code my own functions for the other methods for which functions do not exist.

# Methodology


# Data

Download the  file:

[estimating_quartiles.csv](https://drive.google.com/open?id=1Nc_VFXo2SrsSdprfCmQYhLbJawAzKpH6)

# References

[numpy.quantile](https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.quantile.html?highlight=quantile)

[scipy.stats.mstats.mquantiles](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mstats.mquantiles.html)

# License

Copyright (c) 2018 GILLES PILON <gillespilon13@gmail.com>.

Permission to use, copy, modify, and distribute this software for any purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

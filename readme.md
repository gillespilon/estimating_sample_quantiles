<!--
[![Coverity Scan Build Status](https://img.shields.io/coverity/scan/10257.svg)](https://scan.coverity.com/projects/gillespilon-estimating_sample_quantiles)
[![Travis](https://img.shields.io/travis/rust-lang/rust.svg)](https://travis-ci.org/gillespilon/estimating_sample_quantiles)
-->

# In brevi

The purpose of this repository is to illustrate the many methods to estimate sample quantiles. This arose while comparing results from NumPy with Minitab statistical software, which led to questions of why the difference. This is important to me because the differences in Q1 and Q3 lead to practically significant differences in estimates of the confidence intervals of Q2.

I use functions from NumPy and SciPy to estimate quantiles. I might have to code my own functions for the other methods for which functions do not exist.

# Explanation of the eleven methods

Quantiles divide the range of a probability distribution into continuous intervals with equal probabilities, or divide the observations in a sample in the same way [Wikipedia](https://en.wikipedia.org/wiki/Quantile). A sample drawn from an unknown population requires estimating the quantiles. There are twelve known methods that commonly appear in statistical packages. Methods 1-3 are based on rounding. Methods 4-9 are based on linear interpolation.

The data are sorted in increasing order. Each method computes $Q_{\text{p}}$, the estimate for the $k^{th}$ $q$-quantile, where $p = k/q$, from a sample of size $N$ by computing a real-valued index $h$. When $h$ is an integer, the $h^{th}$ smallest of the $N$ values, $x_h$, is the quantile estimate. Otherwise, a rounding or interpolation scheme is used to compute the quantile estimate from $h$, $x_{\lfloor \text{h}\rfloor}$, and $x_{\lceil \text{h}\rceil}$.

Sample quantiles are defined by:

$$
\begin{equation}
Q_p = (1 - \gamma) \space x_j \space + \space \gamma \space x_{\text{j+1}}
\end{equation}
$$

where:

$$
\begin{equation}
x_j \text{ is the } j^{th} \text{ order statistic}\\
\end{equation}
$$

$$
\begin{equation}
\gamma \text{ is a function of } j = \lfloor \text{(n} \times \text{p + m)} \rfloor\\
\end{equation}
$$

$$
\begin{equation}
m = \text{alphap + p } \times \text{(1} - \text{alphap} - \text{betap)}\\
\end{equation}
$$

$$
\begin{equation}
g = \text{n} \times \text{p} + \text{m} - \text{j}\\
\end{equation}
$$

$$
\begin{equation}
\frac{j - m}{n} \leq p \lt \frac{j - m + 1}{n}\\
\end{equation}
$$

Reinterpreting the above equations to compare to <b>R</b> gives:

$$
\begin{equation}
p(k) = \frac{k - \text{alphap}}{n + 1 - \text{alphap} - \text{betap}}
\end{equation}$$

In the script I am particularly interested in the 4-quantiles, called the 1<sup>st</sup>, 2<sup>nd</sup> and 3<sup>rd</sup> quartiles (Q1, Q2. Q3).

The following table is a work in progress, to combine the eleven methods into one table.

<table>
<tbody style="font-size: 8px";>
<tr>
<th style="text-align:center">Method</th>
<th style="text-align:center">Software</th>
<th style="text-align:center">$h$</th>
<th style="text-align:center">$Q_p$</th>
<th style="text-align:center">SciPy (alphap, betap)</th>
<th style="text-align:center">Notes</th>
</tr>
<tr>
<td style="text-align:center">1</td>
<td>R-1, SAS-3</td>
<td>$Np + \frac{1}{2}$</td>
<td>$x_{\lceil \text{h} - \frac{1}{2}\rceil}$</td>
<td></td>
<td>Inverse of empirical cumulative distribution function (CDF). When $p = 0$, use $x_1$.</td>
</tr>
<tr>
<td style="text-align:center">2</td>
<td>R-2, SAS-5</td>
<td>$Np + \frac{1}{2}$</td>
<td>$\frac{x_{\lceil \text{h} - \frac{1}{2}\rceil} + x_{\lfloor \text{h} + \frac{1}{2}\rfloor}}{2}$</td>
<td></td>
<td>The same as R-1, but with averaging at discontinuities. When $p = 0$, use $x_1$.When $p = 1$, use $x_N$.</td>
</tr>
<tr>
<td style="text-align:center">3</td>
<td>R-3, SAS-2</td>
<td>$Np$</td>
<td>$x_{\lfloor \text{h}\rceil}$</td>
<td></td>
<td>The observation numbered closest to $Np$ (piecewise linear function). It is also called the nearest even-order statistic. Here, $\lfloor \text{h}\rceil$ indicates rounding to the nearest integer, choosing the even integer in the case of a tie. When $p \leq \frac{\frac{1}{2}}{N}$, use $x_1$.</td>
</tr>
<tr>
<td style="text-align:center">4</td>
<td>R-4, SAS-1</td>
<td>$Np$</td>
<td>$x_{\lfloor \text{h}\rfloor} + (h - \lfloor \text{h} \rfloor) (x_{\lfloor \text{h} \rfloor + 1} - x_{\lfloor \text{h} \rfloor})$</td>
<td>(0,1)</td>
<td>$\frac{k}{n}$ Linear interpolation of the emperical distribution function. When $p \lt \frac{1}{N}$, use $x_1$. When $p = 1$, use $x_N$.</td>
</tr>
<tr>
<td style="text-align:center">5</td>
<td>R-5</td>
<td>$Np + \frac{1}{2}$</td>
<td>$x_{\lfloor \text{h}\rfloor} + (h - \lfloor \text{h} \rfloor) (x_{\lfloor \text{h} \rfloor + 1} - x_{\lfloor \text{h} \rfloor})$</td>
<td>(0.5,0.5)</td>
<td>$\frac{k - \frac{1}{2}}{n}$ Piecewise linear function where the knots are the values midway through the steps of the emperical distribution function. When $p \lt \frac{\frac{1}{2}}{N}$, use $x_1$. When $p \geq \frac{(N - \frac{1}{2}}{N})$, use $x_N$.</td>
</tr>
<tr>
<td style="text-align:center">6</td>
<td>R-6, SAS-4 Minitab, SPSS</td>
<td>$(N + 1)p$</td>
<td>$x_{\lfloor \text{h}\rfloor} + (h - \lfloor \text{h} \rfloor) (x_{\lfloor \text{h} \rfloor + 1} - x_{\lfloor \text{h} \rfloor})$</td>
<td>(0,0)</td>
<td>$\frac{k}{n +1}$ Linear interpolation of the expectations for the order statistics for the uniform distribution on [0,1]. That is, it is the linear interpolation between points $p_h$ and $x_h$, where $p_h = \frac{h}{N+ 1}$ is the probability that the last of $(N + 1)$ randomly drawn values will not exceed the $h^\text{th}$ smallest of the first $N$ randomly drawn values. When $p \lt \frac{1}{N + 1}$, use $x_1$. When $p \geq \frac{N}{N + 1}$, use $x_N$.</td>
</tr>
<tr>
<td style="text-align:center">7</td>
<td>R-7</td>
<td>$(N - 1)p + 1$</td>
<td>$x_{\lfloor \text{h}\rfloor} + (h - \lfloor \text{h} \rfloor) (x_{\lfloor \text{h} \rfloor + 1} - x_{\lfloor \text{h} \rfloor})$</td>
<td>(1,1)</td>
<td>$p(k) = \frac{k - 1}{n - 1}\\ p(k) = \text{mode[F(x[k])]}$<br />Linear interpolation of the modes for the order statistics for the uniform distribution on [0,1].  When $p = 1$, use $x_N$.</td>
</tr>
<tr>
<td style="text-align:center">8</td>
<td>R-8</td>
<td>$(N + \frac{1}{3})p + \frac{1}{3}$</td>
<td>$x_{\lfloor \text{h}\rfloor} + (h - \lfloor \text{h} \rfloor) (x_{\lfloor \text{h} \rfloor + 1} - x_{\lfloor \text{h} \rfloor})$</td>
<td>$(\frac{1}{3},\frac{1}{3})$</td>
<td>$p(k) = \frac{k - \frac{1}{3}}{n + \frac{1}{3}}$ Then $p(k) \text{ ~ median}{[F(x[k])]}.$ The resulting quantile estimtes are approximately median-unbiased regardless of the distribution of x. Linear interpolation of the approximate medians for order statistics. When $p \lt \frac{\frac{2}{3}}{N + \frac{1}{3}}$, use $x_1$. When $p \geq \frac{(N - \frac{1}{3})}{(N + \frac{1}{3})}$, use $x_N$.</td>
</tr>
<tr>
<td style="text-align:center">9</td>
<td>R-9</td>
<td>$(N + \frac{1}{4})p + \frac{3}{8}$</td>
<td>$x_{\lfloor \text{h}\rfloor} + (h - \lfloor \text{h} \rfloor) (x_{\lfloor \text{h} \rfloor + 1} - x_{\lfloor \text{h} \rfloor})$</td>
<td>$(\frac{3}{8},\frac{3}{8})$</td>
<td>$p(k) = \frac{k - \frac{3}{8}}{n + \frac{1}{4}}$ Blom. The resulting quantile estimates are approximately unbiased for the expected order statistics if $x$ is normally distributed. When $p \lt \frac{\frac{5}{8}}{N + \frac{1}{4}}$, use $x_1$. When $p \geq \frac{N - \frac{3}{8}}{N + \frac{1}{4}}$, use $x_N$.</td>
</tr>
<tr>
<td style="text-align:center">10</td>
<td></td>
<td></td>
<td></td>
<td>(0.4,0.4)</td>
<td>Cunnane's approximately quantile unbiased definition.</td>
</tr>
<tr>
<td style="text-align:center">11</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Filliben's estimate.</td>
</tr>
<tr>
<td style="text-align:center">12</td>
<td></td>
<td></td>
<td></td>
<td>(0.35,0.35)</td>
<td>APL, used with PWM.</td>
</tr>
</tbody>
</table>

# Software

As shown above, R (version 2.0.0 onwards) implements methods 1-9. SciPy implements methods 4-9, 10, and a method called APL (need info on this).[scipy.stats.mstats.mquantiles](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mstats.mquantiles.html)

# References

[datasense module](https://github.com/gillespilon/datasense).

[Five-number summary](https://en.wikipedia.org/wiki/Five-number_summary).

Hyndman, Rob J. and Yanan Fan. "Sample Quantiles in Statistical Packages." *The American Statistician* Vol. 50, No. 4 (Nov. 1996): 361-365. [JSTOR 2684934](http://www.jstor.org/stable/2684934).

McGill, Robert, John W. Tukey, and Wayne A. Larsen. 1978. "Variations of Box Plots." *The American Statistician 21 (February 1978), no. 1; 12-16. [https://www.jstor.org/stable/2683468](https://www.jstor.org/stable/2683468).

[pandas](https://pandas.pydata.org/pandas-docs/stable/api.html).

[R documentation on quantiles](https://www.rdocumentation.org/packages/stats/topics/quantile).

[R quantile function](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/quantile.html).

[SciPy documentation on mquantiles](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mstats.mquantiles.html).

[SciPy documentation on masked arrays](https://numpy.org/doc/stable/reference/maskedarray.html).

Wikipedia. "Quantile". Last modified 2018-08-01. [https://en.wikipedia.org/wiki/Quantile](https://en.wikipedia.org/wiki/Quantile).

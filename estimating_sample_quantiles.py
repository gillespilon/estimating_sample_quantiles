#! /usr/bin/env python3
"""
Estimating sample quantiles
"""

import scipy.stats.mstats as ms
import datasense as ds
import pandas as pd


def main():
    data = {"y": [0, 0, 1, 2, 63, 61, 27, 13]}
    df = pd.DataFrame(data=data)
    series_name_y = "y"
    print("pandas.Series.describe():")
    print()
    print(df[series_name_y].describe())
    print()
    method06 = ms.mquantiles(
        df[series_name_y],
        prob=(0.25, 0.50, 0.75),
        alphap=0,
        betap=0
    )
    print("R method 6, SPSS, Minitab:")
    print(method06)
    print()
    method07 = ms.mquantiles(
        df[series_name_y],
        prob=(0.25, 0.50, 0.75),
        alphap=1,
        betap=1
    )
    print(
        "R method 7 default, Splus 3.1, pandas default, NumPy default linear:"
    )
    print(method07)
    print()
    method08 = ms.mquantiles(
        df[series_name_y],
        prob=(0.25, 0.50, 0.75),
        alphap=1/3,
        betap=1/3
    )
    print("R method 8, NumPy median_unbiased, datasense:")
    print(method08)
    print()
    method10 = ms.mquantiles(
        df[series_name_y],
        prob=(0.25, 0.50, 0.75),
        alphap=.4,
        betap=.4
    )
    print("Cunane's method, SciPy default")
    print(method10)
    print()
    print("ds.nonparametric_summary()")
    series = ds.nonparametric_summary(series=df[series_name_y])
    print(series)
    print()


if __name__ == "__main__":
    main()

#! /usr/bin/env python3
"""
Estimating sample quantiles
"""

import scipy.stats.mstats as ms
import datasense as ds
import pandas as pd


def main():
    OUTPUT_URL = "estimating_sample_quantiles.html"
    HEADER_TITLE = "Estimating Sample Quantiles"
    DATA = {"y": [0, 0, 1, 2, 63, 61, 27, 13]}
    HEADER_ID = "estimating-sample-quantiles"
    PROB = (0.25, 0.50, 0.75)
    SERIES_NAME_Y = "y"
    original_stdout = ds.html_begin(
        output_url=OUTPUT_URL,
        header_title=HEADER_TITLE,
        header_id=HEADER_ID
    )
    df = pd.DataFrame(data=DATA)
    print("pandas.Series.describe():")
    print(df[SERIES_NAME_Y].describe())
    print()
    method06 = ms.mquantiles(
        df[SERIES_NAME_Y],
        prob=PROB,
        alphap=0,
        betap=0
    )
    print("R method 6, SPSS, Minitab:")
    print(method06)
    print()
    method07 = ms.mquantiles(
        df[SERIES_NAME_Y],
        prob=PROB,
        alphap=1,
        betap=1
    )
    print(
        "R method 7 default, Splus 3.1, pandas default, NumPy default linear:"
    )
    print(method07)
    print()
    method08 = ms.mquantiles(
        df[SERIES_NAME_Y],
        prob=PROB,
        alphap=1/3,
        betap=1/3
    )
    print("R method 8, NumPy median_unbiased, datasense:")
    print(method08)
    print()
    method10 = ms.mquantiles(
        df[SERIES_NAME_Y],
        prob=PROB,
        alphap=.4,
        betap=.4
    )
    print("Cunane's method, SciPy default")
    print(method10)
    print()
    print("ds.nonparametric_summary()")
    series = ds.nonparametric_summary(series=df[SERIES_NAME_Y])
    print(series)
    print()
    ds.html_end(
        original_stdout=original_stdout,
        output_url=OUTPUT_URL
    )


if __name__ == "__main__":
    main()

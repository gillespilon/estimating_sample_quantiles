#!/usr/bin/env python3

'''
Estimating sample quantiles
'''

# time -f '%e' ./estimating_sample_quantiles.py > estimating_sample_quantiles.txt
# ./estimating_sample_quantiles.py > estimating_sample_quantiles.txt


import pandas as pd
import scipy.stats.mstats as ms
from scipy.stats import anderson
import scipy.stats as sm
import statsmodels.stats.diagnostic as smd
import numpy as np

import datasense as ds

# y is the column of response values.
df = pd.read_csv('estimating_sample_quantiles.csv')

# Calculate basic statistics.
df.describe()


resultd = ms.mquantiles(df['y'], prob=(0.25, 0.50, 0.75), alphap=0.33, betap=0.33)
resultd


resultd[0]


resultminitab = ms.mquantiles(df['y'], prob=(0.25, 0.50, 0.75), alphap=0, betap=0)
resultminitab


ds.nonparametric_summary(df['y']) # alphap=0.33 betap=0.33 by default
ds.nonparametric_summary(df['y'], alphap=0, betap=0) # Minitab
df.min()
df.max()
df.mean()
df.std()
df.var()
df.skew()
df.kurt()
df.count()


adresult = anderson(df['y'], dist='norm')
adresult.statistic


smd.normal_ad(df['y'])


sm.norm.interval(0.95,
                 loc=np.mean(df['y']),
                 scale=sm.sem(df['y']))


sm.t.interval(0.95,
              len(df['y']-1),
              loc=np.mean(df['y']),
              scale=sm.sem(df['y']))

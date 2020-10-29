# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 16:54:23 2020

@author: SWannell
"""

from scipy.stats import ttest_ind_from_stats
from scipy.stats import ttest_ind
from scipy.stats import t as ttest
import numpy as np
import pandas as pd

df = pd.read_csv('AmendedData\\GAgiftvaluedata.csv')

df = df[df['value'] <= 100]
ctrl_val_desc = df[df['expid'] == 'ctrl'].describe()
test_val_desc = df[df['expid'] == 'test'].describe()

# =============================================================================
# Compute the t-test
# =============================================================================

t, p = ttest_ind_from_stats(
            ctrl_val_desc.loc['mean', 'value'],
            ctrl_val_desc.loc['std', 'value'],
            ctrl_val_desc.loc['count', 'value'],
            test_val_desc.loc['mean', 'value'],
            test_val_desc.loc['std', 'value'],
            test_val_desc.loc['count', 'value'],
            )

degf = df.describe().loc['count', 'value'] - 2

print("Control: (Mean=", round(ctrl_val_desc.loc['mean', 'value'], 0),
      ", Std Dev=", round(ctrl_val_desc.loc['std', 'value'], 0),
      ")\nTest: (Mean=", round(test_val_desc.loc['mean', 'value'], 0),
      ", Std Dev=", round(test_val_desc.loc['std', 'value'], 0),
      ")\nt(", degf, ")=", round(t, 2), ", p=", round(p, 2))

# =============================================================================
# Compute the CI on the difference
# =============================================================================


def welch_ttest(x1, x2):
    """Compute Welch's t-test on two samples"""
    n1 = x1.size
    n2 = x2.size
    m1 = np.mean(x1)
    m2 = np.mean(x2)
    v1 = np.var(x1, ddof=1)
    v2 = np.var(x2, ddof=1)
    # Pool
    pooled_se = np.sqrt(v1/n1 + v2/n2)
    delta = m1-m2
    # t-test stats
    tstat = delta / pooled_se
    df = (v1 / n1 + v2 / n2)**2 / (v1**2 / (n1**2 * (n1 - 1)) + v2**2 / (n2**2 * (n2 - 1)))
    # two side t-test
    p = 2 * ttest.cdf(-abs(tstat), df)
    # upper and lower bounds
    lb = delta - ttest.ppf(0.975, df)*pooled_se
    ub = delta + ttest.ppf(0.975, df)*pooled_se

    return pd.DataFrame(np.array([tstat, df, p, delta, lb, ub]).reshape(1, -1),
                        columns=['T statistic', 'df', 'pvalue 2 sided',
                                 'Difference in mean', 'lb', 'ub'])

    
welch = welch_ttest(df[df['expid'] == 'test']['value'].values,
                    df[df['expid'] == 'ctrl']['value'].values)

print(welch.T)

welch.loc[0, 'ctrl_mean'] = ctrl_val_desc.loc['mean', 'value']
welch.loc[0, 'ctrl_vol'] = ctrl_val_desc.loc['count', 'value']
welch.loc[0, 'test_mean'] = test_val_desc.loc['mean', 'value']
welch.loc[0, 'test_vol'] = test_val_desc.loc['count', 'value']

welch.to_csv('AmendedData\\WelchTtest.csv', index=False)

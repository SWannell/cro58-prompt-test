# -*- coding: utf-8 -*-
"""
Created on Thu May 14 15:58:44 2020

@author: SWannell
"""

import pandas as pd

fp = 'RawData\\CRO58 gift values - CRO58_giftvals.csv'
df = pd.read_csv(fp, skiprows=14)
df.dropna(inplace=True)
df.columns = ['id', 'expid', 'count', 'value']
expid = "p1QJ_NkPQ9upbkKUn--OhQ"
exp_codes = {expid + ':0': 'ctrl',
             expid + ':1': 'test'}
df['expid'] = df['expid'].replace(exp_codes)
df.to_csv('AmendedData\\GAgiftvaluedata.csv', index=False)
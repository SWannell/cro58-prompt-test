# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 14:51:09 2020

@author: SWannell
"""

import pandas as pd

df = pd.read_csv('AmendedData\\WelchTtest.csv')
df = df[['lb', 'ub', 'ctrl_mean', 'ctrl_vol', 'test_mean', 'test_vol']]

df['test_lb_mean'] = df.loc[0, 'ctrl_mean'] + df.loc[0, 'lb']
df['test_ub_mean'] = df.loc[0, 'ctrl_mean'] + df.loc[0, 'ub']
df['test_lb_vol'] = df['test_vol']
df['test_ub_vol'] = df['test_vol']

rows = ['ctrl', 'test_lb', 'test_ub']
cols = {row: [col for col in df.columns if row in col] for row in rows}


modest = 12.44
hopeful = 30
em_rate = 0.15  # Conservative assumption

projected = pd.DataFrame(index=rows,
                         columns=['upfront', 'modest', 'hopeful'])

for row in rows:
    col = cols[row]
    projected.loc[row, 'upfront'] = df[col].product(axis=1)[0]
    em_vol = df.loc[0, '{}_vol'.format(row)] * em_rate
    projected.loc[row, 'modest'] = em_vol*modest + projected.loc[row,
                                                                 'upfront']
    projected.loc[row, 'hopeful'] = em_vol*hopeful + projected.loc[row,
                                                                   'upfront']

print(projected)

projected.to_csv('AmendedData\\IncomeProjections.csv')

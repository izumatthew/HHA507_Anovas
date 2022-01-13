#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 12:40:31 2022

@author: izuchukwumatthew
"""

def rules(row):
  if row['COVID-19_Deaths'] <= 5000 :
    return 'abnormal'
  elif row['COVID-19_Deaths'] <= 25000:
    return 'normal'
  elif row ['COVID-19_Deaths'] > 45000:
    return 'high'


def['COVID-19 Deaths_mod2'] = df.apply(rules,1)

df[['COVID-19 Deaths', 'COVID-19 Deaths_mod2']]

Is there significance between the number of COVID Deaths and age group?

model = ols('COVID-19 Deaths ~ C(Age Group)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=1)
anova_table

Is there significance between the number of COVID Deaths and age group?


model = ols('anaemia ~ C(smoking)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=1)
anova_table

Is there significance between the number of COVID Deaths and age group?


model = ols('anaemia ~ C(smoking)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=1)
anova_table
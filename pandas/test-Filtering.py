import pandas as pd
import numpy as np
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
print(df.head()) #

df = titanic.loc[0:9, ['age', 'fare']]
print(df)

df2 = df[ df['age'] < 20 ] # boolean indexing
print(df2)

mask1 = (titanic.age >= 10) & (titanic.age < 20)
df_teenage = titanic[mask1]
print(df_teenage.head())

mask2 = (titanic.age < 10) & (titanic.sex == 'female')
df_female_under10 = titanic.loc[mask2]
print(df_female_under10.head())

mask3 = (titanic.age >= 60) | (titanic.age < 10)
df_under10_morethan60 = titanic.loc[mask3, ['age', 'sex', 'alone']]
print(df_under10_morethan60.head())

df['age_under_20'] = df['age'] < 20
print(df.head())

df2 = df.query('age < 20')
print(df2)

df2 = df.query('age >= 20 and fare < 15')
print(df2)

df2 = df.query('age >= 20 or fare < 15')
print(df2)

pd.set_option('display.max_columns', 10)
mask1 = titanic['embark_town'] == 'Southampton'
mask2 = titanic['embark_town'].str.match('Queenstown') # .str로 문자열 접근
df_boolean = titanic[mask1 | mask2]
print(df_boolean.head())

isin_filter = titanic['embark_town'].isin(['Southampton', 'Queenstown'])
df_isin = titanic[isin_filter]
print(df_isin.head())

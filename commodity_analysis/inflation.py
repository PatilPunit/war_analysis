import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sea
path='/home/punit/Downloads/Mint/decode/dataset/global_inflation_countries.csv'
df=pd.read_csv(path)
df=df[['country_code','country_name','region','year','inflation_rate']]
print(df)

print(df['region'].value_counts())
df=df[(df['year'] >= 2012) & (df['year']<2026)]
print(df)
inflation=df.groupby(['region','year']) ['inflation_rate'].mean().reset_index()
# inflation['Year']=inflation[(inflation['Year']>'2020') &(inflation['Year']<'2026')]
print(inflation)
sea.set_style('whitegrid')
plt.figure(figsize=(12,6))
sea.lineplot(data=inflation,x='year',y='inflation_rate',hue='region')
plt.show()

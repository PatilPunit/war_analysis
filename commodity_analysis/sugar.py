import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sea
path = "/home/punit/Downloads/Mint/decode/dataset/commodity_prices.csv"

df = pd.read_csv(path)


df=df[['sugar_eu','sugar_us','sugar_world','date']]
df.rename(columns={'sugar_eu':'se','sugar_us':'su','sugar_world':'sw'},inplace=True)
df['Date']=pd.to_datetime(df['date'])
sugar=df.melt(id_vars='Date',value_vars=['se','su','sw'],var_name='region',value_name='price')
sugar=sugar[(sugar['Date']>='2012')&(sugar['Date'].dt.year<=2022)]
print(sugar)

sea.set_style('whitegrid')
plt.figure(figsize=(12,6))
sea.lineplot(data=sugar,x='Date',y='price',hue='region')
plt.axvline(pd.to_datetime('2021-11-01'),linestyle='--',color='red')
plt.xticks(rotation=90)
plt.show()

before =sugar[sugar['Date']>'2021-11-01'] ['price'].mean()
after = sugar[sugar['Date']<'2021-11-01'] ['price'].mean()
print(before)
print(after)
print(sugar.loc[sugar['price'].idxmax()])
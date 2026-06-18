import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sea
path = "/home/punit/Downloads/Mint/decode/dataset/commodity_prices.csv"

df = pd.read_csv(path)

print('_'*145)
df=df[['oil_brent','date']]
df.rename(columns={'oil_brent':'price'},inplace=True)
df['Date']=pd.to_datetime(df['date'])
oil=df[(df['price']>0) & (df['Date'].dt.year >=2012) & (df['Date'].dt.year<=2026)]
sea.set_style('whitegrid')
plt.figure(figsize=(12,6))
sea.lineplot(data=oil,x='Date',y='price',markers='o')
plt.axvline(pd.to_datetime('2022-06-01'),color='red',linestyle='--',label='War Begin')
plt.xticks(rotation=65)
plt.show()

before= oil[oil['Date'] < '2022-06-01'] ['price'].mean()
after= oil[oil['Date'] > '2022-06-01'] ['price'].mean()
print(before)
print(after)
print(oil.loc[oil['price'].idxmax()])
print('_'*145)


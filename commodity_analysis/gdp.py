import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sea
path='/home/punit/Downloads/Mint/decode/dataset/Global Economy Indicators.csv'
df=pd.read_csv(path)

df=df[[' Country ', ' Year ',' Agriculture, hunting, forestry, fishing (ISIC A-B) ',' Imports of goods and services ',' Gross Domestic Product (GDP) ']]

df.rename(columns={' Country ':'country',' Agriculture, hunting, forestry, fishing (ISIC A-B) ':'Agriculture',' Imports of goods and services ':'import',' Gross Domestic Product (GDP) ':'GDP',' Year ':'year'},inplace=True)
print(df)
df=df[(df['year']>2012)&(df['year']<2026)]
gdp=df.groupby(['year','country'])   ['GDP'].mean().reset_index()
pd.DataFrame(gdp)
print(type(gdp))

plt.figure(figsize=(12,6))
sea.set_style('whitegrid')
sea.barplot(data=gdp,x='year',y='GDP')
plt.xticks(rotation=90)

plt.yticks(rotation=20)
plt.show()
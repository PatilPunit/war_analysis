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

agri=df.groupby(['country','year']) ['Agriculture'].mean().reset_index()

plt.figure(figsize=(18,6))
sea.set_style('whitegrid')
sea.lineplot(data=agri,x='year',y='Agriculture',hue='country')
plt.show()
sea.barplot(data=agri,x='year',y='Agriculture')
plt.show()
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 12:06:39 2024

@author: thean
"""

#importing pandas
import pandas as pd
import matplotlib.pyplot as plt

#importing excel file
df = pd.read_excel('amazon.xlsx')

#print first 5 rows
print(df.head())

#create new column that calculates cost price
df["cost_price"] = df['discounted_price'] * df['cost_percentage']

#create column that calculates profit
df["profit"] = df['discounted_price'] - df['cost_price']

#calculate profit margin = (discounted_price - cost_price)/cost_price
df["profit_margin"] = (df['discounted_price'] - df['cost_price']) / df['cost_price']

#droping a column
df = df.drop('cost_percentage', axis=1)

#creating a top 10 table which shows highest selling products
top_10 = df.sort_values('discounted_price', ascending=False)
top_10 = top_10.head(10)

#creating an alert column where if rating is less than 4, alert is low.
df.loc[df['rating'] <= 4, 'Alert'] = 'Low'
df.loc[df['rating'] > 4, 'Alert'] = 'High'

#creating a chart
ax = top_10.plot.bar(x = 'product_id', y = 'discounted_price', rot=90, color= 'blue')
ax.set_xlabel('Product ID')
ax.set_ylabel('Discounted Price')
ax.set_title('Discounted Price per Product ID')
plt.show()

#export tables to excel
df.to_excel('final_amazon_table.xlsx', index=False)
top_10.to_excel('top_10_products.xlsx', index=False)
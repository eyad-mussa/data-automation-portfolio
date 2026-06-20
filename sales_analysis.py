
import pandas as pd
supermarket_df=pd.read_csv("supermarket_sales.csv")
print("Shape:",supermarket_df.shape)
print("\nColumn info:")
print(supermarket_df.info())
print("\nStatistical summary:")
print(supermarket_df.describe())
print("\nTotal sales by product line:")
print(supermarket_df.groupby("Product line",)['Sales'].sum().sort_values(ascending=False))
print("\nAverage rating by branch:")
print(supermarket_df.groupby("Branch")['Rating'].mean().round(2))
print("\nTotal revenue by payment method:")
print(supermarket_df.groupby("Payment")['Sales'].sum().sort_values(ascending=False))
print("\nMissing values per column:")
print(supermarket_df.isnull().sum())


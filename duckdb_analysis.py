import duckdb
import pandas as pd
###########################
#initiating the engine
###########################
df = pd.read_csv('supermarket_sales.csv')
the_from="read_csv_auto('supermarket_sales.csv')"
conn = duckdb.connect()
###########################
#Shape of the dataset
###########################
print("Shape:", df.shape)
######################################################
#Total sales by product line sorted highest to lowest
######################################################
result1=conn.execute(f'SELECT "Product line" as"Product line",sum(Sales) AS "total sales" FROM {the_from}  GROUP BY "Product line" ORDER BY sum(Sales) desc').df()
print("\nTotal sales by product line:")
print(result1.to_string(index=False))
######################################################
#Average rating by branch rounded to 2 decimal places
######################################################
result2=conn.execute(f'SELECT Branch,round(mean(Rating),2) AS "Average rating" FROM {the_from}  GROUP BY Branch ORDER BY mean(Rating) desc').df()
print("\nAverage rating by branch:")
print(result2.to_string(index=False))
#############################################################
#Total revenue by payment method sorted highest to lowest
#############################################################
result3=conn.execute(f'SELECT Payment,sum(Sales) AS "total revenue" FROM {the_from}  GROUP BY Payment ORDER BY sum(Sales) desc').df()
print("\nTotal revenue by payment method:")
print(result3.to_string(index=False))
###########################
#Top 5 rows
###########################
result4 = conn.execute(f"SELECT * FROM {the_from} LIMIT 5").df()
print("\nTop 5 rows of the dataset:")
print(result4.to_string(index=False))
#################################
#Missing values count per column
#################################
print("\nMissing values per column:")
print(df.isnull().sum())
import pandas as pd
import sqlite3 as sq
###########################
#initiating the engine
###########################
retail_df=pd.read_csv("supermarket_sales.csv")
retail_db=sq.connect("retail_sql.db")
retail_df.to_sql("sales", retail_db, if_exists="replace", index=False)
cur = retail_db.cursor()
###########################
#1st requirement
###########################
rows=cur.execute("select count(*) from sales")
rows_num=rows.fetchone()[0]
columns=cur.execute(" pragma table_info('sales') ")
columns_num=len(columns.fetchall())
print(f"Shape:({rows_num},{columns_num})")
###########################
#2nd requirement
###########################
query2='select "Product line" , sum(Sales) as "total sales" from sales group by "Product line" order by sum(Sales) desc '
table2 = pd.read_sql_query(query2, retail_db)
print("\nTotal sales by product line:")
print(table2.set_index('Product line').to_string())
###########################
#3rd requirement
###########################
query3='select Branch, round(avg(Rating),2) as "average rating" from sales group by Branch '
table3 = pd.read_sql_query(query3, retail_db)
print("\nAverage rating by branch:")
print(table3.set_index('Branch').to_string())
###########################
#4th requirement
###########################
query4='select Payment,sum(Sales) as "total revenue" from sales group by payment order by sum(Sales) desc'
table4 = pd.read_sql_query(query4, retail_db)
print("\nTotal revenue by payment method:")
print(table4.set_index('Payment').to_string())
###########################
#5th requirement
###########################
query5='select * from sales limit 5;'
table5 = pd.read_sql_query(query5, retail_db)
print("\nTop 5 rows of the dataset:")
print(table5.to_string(index=False))
###########################
#6th requirement
###########################
print("\nMissing values per column:")
print(retail_df.isnull().sum())
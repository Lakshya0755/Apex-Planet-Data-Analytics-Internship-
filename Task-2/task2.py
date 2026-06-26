import pandas as pd
import sqlite3
df = pd.read_csv("cleaned_dataset.csv")

#Database creation
conn = sqlite3.connect("Internship.db")
df.to_sql("Internship_table", conn, if_exists="replace", index=False)
conn.close()
print("Database created successfully!")

#formatting
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

#EDA

print(df.info()) 
print(df[["Age","Quantity","Unit_Price","Total_Sales"]].describe()) 

""" Describe value dedeta hai bhot sari jese(mean,min,max) jisse hum insight nikalte hai jese ki 
          age max 65 hai min 12 hai to insight hua ki range 12-65 hai  """

#categorical analysis(category wise analyse krege)
"""Value_count() Distinct value ki occurance"""
print(df["Category"].value_counts(),"\n") # gaves occurance of distinct value under category
print(df["City"].value_counts(),"\n")
print(df["Product"].value_counts())



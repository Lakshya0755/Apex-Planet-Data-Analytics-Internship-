# Business Ques 1: Which product generates the highest revenue?
# Business Ques 2: Who are the top 5 customers based on total sales?
# Business Ques 3:What is the total quantity sold for each category?
# Business Ques 4: Which gender contributes more to total sales? 
# Business Ques 6: Which city has the highest total sales?
# Business Ques 7: Which category generates the highest total sales?

import sqlite3
import pandas as pd
conn= sqlite3.connect("Internship.db")
df= pd.read_excel("ApexPlanet_DataAnalytics_Dataset.xlsx")
print(df.info())

Query1="""SELECT Product,
SUM(Total_Sales) AS Total_Revenue
FROM Internship_table
GROUP BY Product
ORDER BY Total_Revenue DESC;"""
result1= pd.read_sql_query(Query1,conn)

Query2="""SELECT Customer_Name,
SUM(Total_Sales) AS Total_Revenue
FROM Internship
GROUP BY Customer_Name
ORDER BY Total_Revenue DESC
LIMIT 5;"""

Query3="""select SUM(Quantity) as total,Category from Internship_table
               group by Category order by total DESC"""

Query6= """select City,SUM(Total_Sales) AS total from Internship_table
group by city
order by total
limit 1;"""

Query4= """SELECT Gender,
SUM(Total_Sales) AS Total_Revenue
FROM Internship_table
GROUP BY Gender
limit 1;"""

Query7="""SELECT Category,
SUM(Total_Sales) AS Total_Revenue
FROM Internship_table
GROUP BY Category
ORDER BY Total_Revenue DESC;"""

result1= pd.read_sql_query(Query1,conn)
result2= pd.read_sql_query(Query2,conn)
result3= pd.read_sql_query(Query3,conn)
result4= pd.read_sql_query(Query4,conn)
result6= pd.read_sql_query(Query6,conn)
result7= pd.read_sql_query(Query7,conn)

print("result is: \n")
print(result1,"\n\n",result2,"\n\n",result3,"\n\n",result4,"\n\n",result6,"\n\n",result7)
import pandas as pd
import numpy as np

#loading file

ex= pd.read_excel("ApexPlanet_DataAnalytics_Dataset - Copy.xlsx")

"""# finding duplicates

print("your duplicat: ",ex.duplicated().sum())

# finding info

print(ex.info())

#finding null values

print(ex.isnull().sum())
ex["Age"]= ex["Age"].fillna(0)
ex["City"]=ex["City"].fillna("N/A") # we can also do ex.fillna()
print(ex.isnull().sum())

#checking format
print(ex["City"].unique())
print(ex.describe())
print(ex["Age"])
"""
print(ex.to_csv())
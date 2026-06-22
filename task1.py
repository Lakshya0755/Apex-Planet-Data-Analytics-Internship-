import pandas as pd

# Load dataset
ex = pd.read_excel("ApexPlanet_DataAnalytics_Dataset - Copy.xlsx")

# Duplicates
print("Duplicates before:", ex.duplicated().sum())
ex = ex.drop_duplicates()
print("Duplicates after:", ex.duplicated().sum())

# Missing values
print(ex.isnull().sum())

# Fill missing values
ex["Age"] = ex["Age"].fillna(0)
ex["City"] = ex["City"].fillna("N/A")

# Standardize text
ex["City"] = ex["City"].str.strip().str.title()

# Date conversion
ex["Order_Date"] = pd.to_datetime(ex["Order_Date"])

# Check unique values
print(ex["City"].unique())

# Statistics
print(ex.describe())

# Save cleaned dataset
ex.to_csv("cleaned_dataset.csv", index=False)

print("Dataset cleaned and saved successfully.")

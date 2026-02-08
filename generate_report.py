import pandas as pd

# Read Excel file
df = pd.read_csv("data/sample_sales.csv")

# Display first rows
print(df.head())

# Simple analysis
total_amount = df["amount"].sum()
print(f"Total sales amount: {total_amount}")
import pandas as pd

df = pd.read_csv("ecommerce_data.csv")

print("Dataset Shape:",df.shape)

print(df.head())

print("\nRevenue")
print(df["Purchase_Amount"].sum())

print("\nAverage Order Value")
print(df["Purchase_Amount"].mean())

print("\nCategory Analysis")
print(df.groupby("Category")["Purchase_Amount"].sum())

from sklearn.cluster import KMeans
import pandas as pd

# Load dataset
df = pd.read_csv("ecommerce_data.csv")

# Select features
X = df[["Purchase_Amount", "Order_Count"]]

# Create KMeans model
kmeans = KMeans(n_clusters=4, random_state=42)

# Generate clusters
df["Cluster"] = kmeans.fit_predict(X)

# Save segmented data
df.to_csv("segmented_customers.csv", index=False)

print(df.head())
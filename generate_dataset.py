import pandas as pd
import numpy as np

np.random.seed(42)

n = 5000

customer_ids = np.arange(1000,1000+n)

categories = [
    'Electronics',
    'Fashion',
    'Home Decor',
    'Books',
    'Sports'
]

data = {
    'Customer_ID': customer_ids,
    'Age': np.random.randint(18,60,n),
    'Gender': np.random.choice(['Male','Female'],n),
    'Category': np.random.choice(categories,n),
    'Purchase_Amount': np.random.randint(500,10000,n),
    'Rating': np.random.uniform(1,5,n).round(1),
    'Order_Count': np.random.randint(1,20,n)
}

df = pd.DataFrame(data)

df.to_csv("ecommerce_data.csv",index=False)

print("Dataset Created Successfully")
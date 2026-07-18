import pandas as pd 

data = {
    "product": ["smartphone","watch","tablet","PC"],
    "price": [200, 50, 350, 700],
    "quantity":[500, 70, 30, 100]
}

df = pd.DataFrame(data)

print(df)
print(df["price"])
print(df.shape)
df["total"] = df["price"] * df["quantity"]

print(f"Total revenue is {df["total"].sum()}")
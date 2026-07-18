import pandas as pd 

data = {
    "name":["john","bob","jeff","bill","john","bob","jeff","bill","jeff"],
    "category": ["phone","watch","laptop","tv" , "tablet","phone","watch","phone","laptop"],
    "amount": [23,33,11,4,5,32,1,23,5]
}


df = pd.DataFrame(data)
total_amounts = df.groupby("category")["amount"].sum()
average_amounts = df.groupby("category")["amount"].mean()

print( total_amounts)
print (average_amounts)


data2 = {
    "name":["john","bob","jeff","bill","john","bob","jeff","bill","jeff"]
}


managers = pd.DataFrame(data2)

merged = managers.merge(df, on="name")

print(merged)

print ( merged.groupby("name")["amount"].sum())
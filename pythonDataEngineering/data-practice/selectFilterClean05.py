import pandas as pd 
import numpy as np


data = {
    "name":["bob","jeff","john"],
    "score":[70, np.nan ,8]
}



df = pd.DataFrame(data)
print(f"{df.isna().sum()} missing values")
df.dropna(subset=["score"])
df = df.drop_duplicates()


df = df[df["score"] >50]
print(df)
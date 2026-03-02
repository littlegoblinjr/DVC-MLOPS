import pandas as pd
import os

data = {"Name": ["John", "Anna", "James", "Linda", "Sounak"],
        "Age": [28, 22, 35, 32, 22],
        "City": ["New York", "Paris", "London", "Berlin", "India"]}


df = pd.DataFrame(data)

new_row_loc = {"Name": "Mansi", "Age": 20, "City": "India"}

df.loc[len(df.index)] = new_row_loc


data_dir = "data"

os.makedirs(data_dir, exist_ok=True)

df.to_csv("data/data.csv", index=False)

print(f"Data saved in {data_dir}/data.csv")
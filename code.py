import pandas as pd
import os

data = {"Name": ["John", "Anna", "James", "Linda"],
        "Age": [28, 22, 35, 32],
        "City": ["New York", "Paris", "London", "Berlin"]}


df = pd.DataFrame(data)


data_dir = "data"

os.makedirs(data_dir, exist_ok=True)

df.to_csv("data/data.csv", index=False)

print(f"Data saved in {data_dir}/data.csv")
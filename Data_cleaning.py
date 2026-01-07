import pandas as pd
df = pd.read_csv("pokemons.csv")

'''
Data_cleaning = process of fixing/removing incomplete,incorrect or irrelevant data.
                close to 75% work done with pandas is data_cleaning.
'''
#df = df.dropna(subset =["Type 2"])
#df = df.fillna({"Type 2": "None"}).replace(), .str.lower()/upper() or we can remove duplicate rows with .drop_duplicates()

print(df.to_string())
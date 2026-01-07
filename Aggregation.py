import pandas as pd

df = pd.read_csv("pokemons.csv")
#Filtering:Keeping a row that matches a condition
#aggregation_functions = Reduces a set of values into a single summary value 
#                        Used to summarize and analyze data
#                        Often used with the groupby() function

#Whole dataframe
#print(df.mean(numeric_only=True))
#print(df.sum(numeric_only=True))
#print(df.min(numeric_only=True))
#print(df.max(numeric_only=True))
#print(df.count(numeric_only=True))

#Single Coloumn
#print(df["HP"].mean())
#print(df["HP"].sum())
#print(df["HP"].min())
#print(df["HP"].max())
#print(df["HP"].count())

group = df.groupby("Type 1")

print(group["HP"].count())

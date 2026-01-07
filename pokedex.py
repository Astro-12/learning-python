import pandas as pd
import numpy as np

pokedex = pd.read_csv("pokemon.csv")

pokedex["Type 2"] = pokedex["Type 2"].fillna["None"]
pokedex = pokedex.drop(columns= ["Total"])

stats = ["HP","Attack","Defense","Sp. Atk", "Sp. Def", "Speed"]
pokedex[stats] = pokedex[stats].apply(pd.to_numeric)

stat_array = pokedex[stats].to_numpy()

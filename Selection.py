#Selection:
import pandas as pd

df = pd.read_csv("pokemons.csv",index_col = "Name")

#Selection_by_coloumn
'''
print(df["Name"].to_string())###.to_string prints the whole data or else pandas automatically prints the first and last 5 coloumns
print(df[["Name","HP","Attack"]].to_string())
'''
#Selection_by_Rows
'''
print(df.loc["Wigglytuff":"Rhyhorn", ["HP","Attack","Defense","Sp. Atk","Sp. Def"]].to_string())
print(df.iloc[0:15:2, 0:4])#0:15:2 represents 0->15_coloumns and odd indexs, 0:4 represent 0 to 4 rows
             ________,_____
            coloumn,  row
'''
pokemon = input("Enter a pokemon name: ")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found")
import pandas as pd

data = {"Name": ["Spongebob", "Patric", "Squidward"],
        "Age" : [30,35,40]
        }

df = pd.DataFrame(data)

#Add a new coloumn
df["Job"] = ["Cook", "N/A", "Cashier"]

#Add a new rows:
new_rows = pd.DataFrame([{"Name": "Lunacy", "Age": 18, "Job": "Engineer"},
                         {"Name": "Adiii", "Age": 19, "Job": "AI_Engineer"}],
                        index =["3","4"])
df = pd.concat([df, new_rows])

print(df)
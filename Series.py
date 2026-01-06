import pandas as pd 
calories = {"Day 1" : 1750, "Day 2" : 2100, "Day 3" : 1700}

series = pd.Series(calories)
"""
print(series)
print(series[series < 1000])
"""
print(series[series < 2000])

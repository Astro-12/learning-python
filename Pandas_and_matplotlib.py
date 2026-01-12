import pandas as pd 
import matplotlib.pyplot as plt

data = {
    'Year': [2018, 2019, 2020, 2021],
    'Sales': [200, 250, 300, 400]
}

df = pd.DataFrame(data)
df.plot(x='Year', y='Sales', kind='line')
plt.show()
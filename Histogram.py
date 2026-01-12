import matplotlib.pyplot as plt
import random

data = [random.randint(1, 100) for _ in range(100)]

plt.hist(data, bins=10)
plt.xlabel("Value Range")
plt.ylabel("Frequency")
plt.title("Histogram Example")

plt.show()
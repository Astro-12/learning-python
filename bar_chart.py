import matplotlib.pyplot as plt
languages = ['Python', 'Java', 'C++', 'JavaScript']
popularity = [90, 70, 60, 75]

plt.bar(languages, popularity)
plt.xlabel("Programming Language")
plt.ylabel("Popularity Score")
plt.title("Language Popularity")

plt.show()
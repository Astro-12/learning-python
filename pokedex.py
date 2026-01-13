import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pokedex = pd.read_csv("pokemon.csv")

pokedex["Type 2"] = pokedex["Type 2"].fillna("None")
pokedex = pokedex.drop(columns=["Total"])

stats = ["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]
pokedex[stats] = pokedex[stats].apply(pd.to_numeric)

stat_array = pokedex[stats].to_numpy()
pokedex["total_stats"] = np.sum(stat_array, axis=1)

weights = np.array([1.0, 1.3, 1.2, 1.4, 1.3, 1.1])
pokedex["power_score"] = stat_array @ weights


def show_top_10():
    top_10 = pokedex.sort_values("total_stats", ascending=False).head(10)
    print(top_10[["Name", "Type 1", "total_stats"]])


def show_type_means():
    type_stats = pokedex.groupby("Type 1")[stats].mean().round(1)
    print(type_stats)


def show_power_scores():
    top_power = pokedex.sort_values("power_score", ascending=False).head(10)
    print(top_power[["Name", "Type 1", "power_score"]])


def search_pokemon():
    query = input("Enter pokemon name: ").strip().lower()

    if not query:
        print("Please enter a name.")
        return
    matches = pokedex[pokedex["Name"].str.lower().str.contains(query)]
    if matches.empty:
        print("❌ Pokemon not found")
    else:
        print(matches[
            ["Name", "Type 1", "Type 2",
             "HP", "Attack", "Defense",
             "Sp. Atk", "Sp. Def", "Speed",
             "total_stats", "power_score"]
        ])
        return
    
    
    print("\n Multiple pokemon found: ")
    for i in enumerate(matches["Name"].values, start = 1):
        print(f"{i}. {__name__}")

    choice = input("\nEnter the number to view details (or press Enter to cancel): ").strip()

    if not choice:
        return
    
    
    choice = int(choice)

    if choice < 1 or choice > len(matches):
        print("⚠️ Number out of range.")
        return

    selected = matches.iloc[choice - 1]

    print("\n📊 Pokémon Details:\n")
    print(selected[
        ["Name", "Type 1", "Type 2",
         "HP", "Attack", "Defense",
         "Sp. Atk", "Sp. Def", "Speed",
         "total_stats", "power_score"]
    ])

def plot_avg_stats_by_type():
    type_stats = pokedex.groupby("Type 1")[stats].mean()

    type_stats.plot(kind="bar", figsize=(12, 6))
    plt.title("Average Pokémon Stats by Type")
    plt.ylabel("Average Stat Value")
    plt.xlabel("Type")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
#Comparing all the stats of all the types seems overwhelming,can be modified so that u can choose any 2 or more pokemons or types to compare the stats for 

def plot_stat_distribution():
    stat = input("Enter stat (HP, Attack, Defense, Speed): ").strip()

    if stat not in stats:
        print("⚠️ Invalid stat name.")
        return

    plt.figure(figsize=(8, 5))
    plt.hist(pokedex[stat], bins=20)
    plt.title(f"{stat} Distribution")
    plt.xlabel(stat)
    plt.ylabel("Number of Pokémon")
    plt.show()
#The graphs can be modified(outline,different colors)basically make the graph more user friendly to understand and again more in-depht selection of what pokemons you wanna compare the stats for

def plot_attack_vs_speed():
    plt.figure(figsize=(8, 6))
    plt.scatter(pokedex["Attack"], pokedex["Speed"])
    plt.title("Attack vs Speed")
    plt.xlabel("Attack")
    plt.ylabel("Speed")
    plt.show()
#The dot color of speed and attack has to be changed.

def menu():
    while True:
        print("\n--- POKEDEX MENU ---")
        print("1. Show Top 10 Pokémon (by Total Stats)")
        print("2. Show Average Stats by Type")
        print("3. Show Top 10 Pokémon (by Power Score)")
        print("4. Search Pokémon by Name")
        print("5. Plot Attack vs Speed")
        print("6. Plot Average Stats by Type")
        print("7. Plot Stat Distribution")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ").strip()

        if not choice.isdigit():
            print("⚠️ Enter a number.")
            continue

        choice = int(choice)

        if choice == 1:
            show_top_10()
        elif choice == 2:
            show_type_means()
        elif choice == 3:
            show_power_scores()
        elif choice == 4:
            search_pokemon()
        elif choice == 5:
            plot_attack_vs_speed()
        elif choice == 6:
            plot_avg_stats_by_type()
        elif choice == 7:
            plot_stat_distribution()
        elif choice == 8:
            print("Goodbye, Trainer! 👋")
            break
        else:
            print("⚠️ Invalid choice.")

menu()

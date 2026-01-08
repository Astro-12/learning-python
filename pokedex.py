import pandas as pd
import numpy as np

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
    name = input("Enter pokemon name: ").strip().lower()
    result = pokedex[pokedex["Name"].str.lower() == name.lower()]
    if result.empty:
        print("❌ Pokemon not found")
    else:
        print(result[
            ["Name", "Type 1", "Type 2",
             "HP", "Attack", "Defense",
             "Sp. Atk", "Sp. Def", "Speed",
             "total_stats", "power_score"]
        ])


def menu():
    while True:
        print("\n--- POKEDEX MENU ---")
        print("1. Show Top 10 Pokémon (by Total Stats)")
        print("2. Show Average Stats by Type")
        print("3. Show Top 10 Pokémon (by Power Score)")
        print("4. Search Pokémon by Name")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            show_top_10()
        elif choice == "2":
            show_type_means()
        elif choice == "3":
            show_power_scores()
        elif choice == "4":
            search_pokemon()
        elif choice == "5":
            print("Goodbye, Trainer! 👋")
            break
        else:
            print("Invalid choice, Try again.")


menu()

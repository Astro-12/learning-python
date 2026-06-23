#Making a inventory merger that merges the inventory of two storehouse together to make a combined unique inventory.
#if a same item exists in both storehouses, the quantity of that item will be added together.

store_1 = {
    "apples": 10,
    "oranges": 5,
    "bananas": 8,
    "grapes": 12,
    "milk" : 20
}

store_2 = {
    "chocolate": 15,
    "cookies": 25,
    "apples": 5,
    "oranges": 10,
    "milk" : 10,
    "Energy Drink" : 30
}
#using dictionary key-valye pairs to store inventory items
#Set Union (|): By converting the keys of both dictionaries into sets and using the | operator, you create a unique collection of every single item name across both stores without duplicates.

def merge_inventories(store_1, store_2):
    merged_inventory = {
        inventory : store_1.get(inventory, 0) + store_2.get(inventory, 0)
        for inventory in set(store_1) | set(store_2)
    }

    return merged_inventory


print(merge_inventories(store_1, store_2))

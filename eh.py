# this project uses python dictionaries to store user information and order details. 
# The users_db dictionary contains user IDs as keys and their corresponding name and city as values. 
# The orders list contains dictionaries with order details, including the order ID, user ID, and order amount.
#write a loop that iterates through the orders list, looks up the corresponding user in the users_db dictionary using the user_id,
# and prints out the user's name, city, and the order amount for each order.

users_db = {
101: {"name": "Aman", "city": "Delhi"},
102: {"name": "Neha", "city": "Mumbai"},
103: {"name": "Rahul", "city": "Bangalore"}
}

orders = [
{"order_id": 1, "user_id": 101, "amount": 2500},
{"order_id": 2, "user_id": 103, "amount": 4200},
{"order_id": 3, "user_id": 101, "amount": 1200}
]


for order in orders:
    user_id = order["user_id"]
    user_info = users_db.get(user_id)
    if user_info:
        name = user_info["name"]
        city = user_info["city"]
        amount = order["amount"]
        print(f"User: {name}, City: {city}, Order Amount: {amount}")
    else:
        print(f"User with ID {user_id} not found.") 
    
print("All orders processed.")

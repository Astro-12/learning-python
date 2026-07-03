#Learning how to untangle a bundled items inside a nested list
#calculate absolute quantity of each product sold in all orders

orders = [
    {"order_id": 1, "items": [{"product": "Laptop", "qty": 1}, {"product": "Mouse", "qty": 2}]},
    {"order_id": 2, "items": [{"product": "Keyboard", "qty": 1}]},
    {"order_id": 3, "items": [{"product": "Mouse", "qty": 1}, {"product": "Keyboard", "qty": 2}]},
    {"order_id": 4, "items": [{"product": "Monitor", "qty": 2}, {"product": "HDMI Cable", "qty": 2}, {"product": "Desk Mat", "qty": 1}]},
    {"order_id": 5, "items": [{"product": "Headphones", "qty": 1}]},
    {"order_id": 6, "items": [{"product": "USB-C Hub", "qty": 1}, {"product": "External SSD", "qty": 1}]},
    {"order_id": 7, "items": [{"product": "Webcam", "qty": 1}, {"product": "Ring Light", "qty": 1}, {"product": "Microphone", "qty": 1}]},
    {"order_id": 8, "items": [{"product": "Wireless Charger", "qty": 3}]},
    {"order_id": 9, "items": [{"product": "Laptop", "qty": 1}, {"product": "Laptop Stand", "qty": 1}]},
    {"order_id": 10, "items": [{"product": "AA Batteries", "qty": 4}, {"product": "Mouse", "qty": 1}]}
]

product_quantities = {}
for order in orders:    #loop through each order in the orders list
    for item in order["items"]:#loop through each item in the items list of the current order
        product = item["product"]#extract the product name from the current item
        qty = item["qty"]#extract the quantity from the current item
        if product in product_quantities:#check if the product is already in the product_quantities dictionary
            product_quantities[product] += qty
        else:#if the product is not in the dictionary, add it with the current quantity
            product_quantities[product] = qty

print("Product Quantities Sold:")
print(product_quantities)

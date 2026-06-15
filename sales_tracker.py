#Making a E-Commerce sales Tracker
#This program will allow the user to input sales data for an e-commerce business, and then it will calculate and display 
# the total revenue, 
# average sales per day, 
# and the best-selling product.

sales_data = [
    {"invoice_id": 101, "category": "Electronics", "price": 799.99, "quantity": 1},
    {"invoice_id": 102, "category": "Clothing", "price": 29.99, "quantity": 4},
    {"invoice_id": 103, "category": "Home & Kitchen", "price": 120.00, "quantity": 2},
    {"invoice_id": 104, "category": "Electronics", "price": 15.50, "quantity": 3},
    {"invoice_id": 105, "category": "Clothing", "price": 49.99, "quantity": 2},
    {"invoice_id": 106, "category": "Home & Kitchen", "price": 15.00, "quantity": 1},
    {"invoice_id": 107, "category": "Electronics", "price": 1200.00, "quantity": 1}
]

def calculate_revenue(sales):
    total_revenue = 0 
    for sale in sales:
        total_revenue += sale["price"] * sale["quantity"]
    return total_revenue

def average_sales_per_day(sales, days):
    total_revenue = calculate_revenue(sales)
    return total_revenue / days

def best_selling_product(sales):
    product_sales = {}
    for sale in sales:
        category = sale["category"]
#tbc

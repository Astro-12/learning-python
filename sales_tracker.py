#Making a E-Commerce sales Tracker
#This program will allow the user to input sales data for an e-commerce business, and then it will calculate and display 
# the total revenue, 
# average sales per day, 
# and the best-selling product.
#Add Average Order Value

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
        quantity = sale["quantity"]
        if category in product_sales:
            product_sales[category] += quantity
        else:
            product_sales[category] = quantity
    best_selling = max(product_sales, key=product_sales.get)
    return best_selling

def average_order_value(sales):
    total_revenue = calculate_revenue(sales)
    total_orders = len(sales)
    if total_orders == 0:
        return 0
    return total_revenue / total_orders

calculate_revenue(sales_data)
average_sales_per_day(sales_data, 7)
best_selling_product(sales_data)
average_order_value(sales_data)

if __name__ == "__main__":
    revenue = calculate_revenue(sales_data)
    avg = average_sales_per_day(sales_data, 7)
    best = best_selling_product(sales_data)
    print(f"Total revenue: ${revenue:.2f}")
    print(f"Average sales per day (7 days): ${avg:.2f}")
    print(f"Best selling category: {best}") 
    print(f"Average order value: ${average_order_value(sales_data):.2f}")   

#Data analysts look for data anomalies or "outliers" 
# (e.g., fraudulent transactions or system glitches) that warp the average metrics.
#The Task: 1. Calculate the average of this list including all numbers.
#2. Write a program that filters the list to create a new list containing only items that are below 100 (normal prices).
#3. Calculate the average of that new filtered list.
#4. Print both averages so you can see how much a couple of massive outliers skew data.

ecom_prices = [45, 50, 62, 48, 55, 1200, 51, 58, 999, 42]

# Step 1: Calculate the average of the original list
average_all = sum(ecom_prices) / len(ecom_prices)

# Step 2: Filter the list to create a new list with items below 100
filtered_prices = [price for price in ecom_prices if price < 100]

# Step 3: Calculate the average of the filtered list
average_filtered = sum(filtered_prices) / len(filtered_prices)

# Step 4: Print both averages 
print ("Average of all prices:", average_all)
print ("Average of filtered prices:", average_filtered)


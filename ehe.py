#
#

with open("raw_data.csv", "r") as file:
    next(file)  
    for line in file:
        row = line.strip().split(",")
        print(row)
#Inside your loop (after you split the line into row), unpack the 5 columns into 5 variables: tx_id, name, product, amount, and status.

#Apply .strip() to name and status to clean up those hidden spaces and that ugly \n.

#Change your print() statement to look like this so we can verify the fix:
#print(name, status)

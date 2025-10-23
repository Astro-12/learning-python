'''
collecting data about the deposit user in putting
collecting the information about the bet
'''
import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 10

ROWS = 3
COLS = 3

SYNBOL_COUNT = {
    "A" : 2,#Rarer 
    "B" : 4,
    "C" : 6,
    "D" : 8 #Common
}

SYMBOL_VALUE = {
    "A" : 10,   
    "B" : 6,
    "C" : 3,
    "D" : 2,
    }

def  get_slot_machine_spin(rows, cols, symbols):\
    #Creating a list of all symbols per column so we can randomly select from them
     all_symbols = []
     for symbol, count in symbol_count.items():
         all_symbols.extend([symbol] * count)
    
     columns = []
     for _ in range(cols):
         current_symbols = all_symbols[:] #Copying the list
         column = []
         for _ in range(rows):
             #choosing a random symbol from the list
             choice = random.choice(current_symbols)
             current_symbols.remove(choice) #no replacement
         column.append(choice)
     return columns 
    
def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number. ")
            
    return amount    

def get_number_of_line():
    while True:
        lines = input("Enter the number of lines to bet on (1 -" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <=  lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number. ")
            
    return lines    

def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number. ")
            
    return amount    

def main():
        balance = deposit()        
        lines = get_number_of_line()
        while True:
            bet = get_bet()
            total_bet = bet * lines 
            
            if total_bet > balance:
                print(f"You do not have enough to bet that amount, your current bet is: ${balance}")
            else:
                break
            
        print(f"You are betting $ {bet} on {lines} lines. Total bet is equal to: ${total_bet}")
        


main()

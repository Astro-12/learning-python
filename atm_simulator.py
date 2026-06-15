#Making an ATM simulator
#Create a variable and set a value and then write a script that keeps running simultaneously
#Create a interface in which a user can
#Check balance
#Deposit money and then integrate it to the balance
#Withdraw money and then integrate it to the balance
balance = 1000  # Initial balance

def deposit_money():    
    global balance
    amount = float(input("Enter the amount to deposit: $"))
    balance += amount
    print(f"Deposit successful. Your new balance is: ${balance}")

def withdraw_money():
    global balance 
    amount = float(input("Enter the amount to withdraw: $"))
    if amount > balance:
        print("Insufficient funds. Please try again.")
    else:
        balance -= amount
        print(f"Withdrawal successful. Your new balance is: ${balance}")

def check_balance():
    print(f"Your current balance is: ${balance}")


def atm_interface():
    while True:
        print("\nWelcome to the ATM Simulator")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Please select an option (1-4): ")

        if choice == '1':
            check_balance()
        elif choice == '2':
            deposit_money()
        elif choice == '3':
            withdraw_money()
        elif choice == '4':
            print("Thank you for using the ATM Simulator. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

atm_interface()

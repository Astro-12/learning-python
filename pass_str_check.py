#Create a variable called password and assign the value "P@ss1517"
#Now, we use for loops and conditional logics to check if the password is strong enough. A strong password should have at 
#least 8 characters, contain both uppercase and lowercase letters, and include at least one number or special character.

def check_password_strength(password):
    has_upper = False
    has_lower = False
    has_special_or_digit = False
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/"

    error_messages = []

    if len(password) < 8:
        error_messages.append("Password must be at least 8 characters long.")

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit() or char in special_characters:
            has_special_or_digit = True
            
    if not has_upper:
        error_messages.append("Password must contain at least one uppercase letter.")
    if not has_lower:
        error_messages.append("Password must contain at least one lowercase letter.")
    if not has_special_or_digit:
        error_messages.append("Password must contain at least one number or special character.")

    if error_messages:
        print("Password is not strong enough:")
        for message in error_messages:
            print(f"- {message}")
    else:
        print("Password is strong.")

password = "p@ss"
check_password_strength(password)        

import random
number_to_guess = random.randint(1, 100)
while True:
        
    try:
        guess = int(input('Choose a number between 1 and 100:'))
        
        if guess < number_to_guess:
            print('Too low!')
        elif guess > number_to_guess:
            print('Too high')
        else:
            print('Congratulations! You have guess the number correctly')
            break
    except ValueError:
        print('Print a valid number')

import random
ROCK = 'r'
PAPER = 'p'
SCISSOR = 's'
emojis = {ROCK: '✊', PAPER: '✋', SCISSOR: '✌️'}
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_input = input('Rock, paper or scissors? (r/p/s): ').lower()
        if user_input in choices:
            return user_input
        else:
            print('Invalid choice')

def display_choices(user_input, computer_choice):
    print(f'You chose {emojis[user_input]}')
    print(f'Computer chose {emojis[computer_choice]}')

def concluding_winner(user_input, computer_choice):
    if (user_input == ROCK and computer_choice == SCISSOR
        or user_input == PAPER and computer_choice == ROCK
        or user_input == SCISSOR and computer_choice == PAPER):
        print('You have won')
    elif user_input == computer_choice:
        print("It's a draw")
    else:
        print('You lose')

while True:
    user_input = get_user_choice()
    computer_choice = random.choice(choices)
    
    display_choices(user_input, computer_choice)
    concluding_winner(user_input, computer_choice)

    while True:
        should_continue = input('Continue? (y/n): ').lower()
        if should_continue == 'y':
            break  
        elif should_continue == 'n':
            exit()
        else:
            print('Please choose an appropriate response (y/n)')

import random

def play_one_round(n):
    # This function processes the human turn.\
    n = play_human_turn(n)
    print('There are ' + str(n) + ' coins on the table.\n')
    if n == 0:
        return 0
    # Then process the computer turn.
    n = play_computer_turn(n)
    if n == 0:
        return 0
    # Prints the number of coins left.
    print('There are ' + str(n) +' coins on the table.\n')
    return n
def play_human_turn(n):
    num_coins = int(input('Will you take 1, 2, or 3 coins? '))
    while num_coins < 1 or num_coins > 3:
        print('Invalid move. Please enter 1, 2, or 3.')
        num_coins = int(input('Will you take 1, 2, or 3 coins? '))
    print('You took ' + str(num_coins) + ' coins.')
    n -= num_coins

    if n == 0:
        print('\nYou took the last coin! You win!')
        return 0
    return n

def play_computer_turn(n):
    
    if n%4 == 0:
        

        possible_moves = []
    for i in range(1, 4):
        if (n - i) % 4 == 0:
            possible_moves.append(i)
    if possible_moves:
        num_coins = random.choice(possible_moves) 
    else:
        num_coins = random.randint(1, 3)

    num_coins = min(num_coins, n) 
    n -= num_coins
    print('\nThe computer took ' + str(num_coins) +' coins.')

    if n == 0:
        print ('The computer took the last coin! You lost!')
        return 0
    return n 
def play_game():
    print('Welcome to the countdown from 21 game!')
    print('There are 21 coins on table.')
    print("One each player's turn, you may remove 1, 2, or 3 coins.")
    print("If a player removes all the coins, they win.")
    print("It's your move.\n")

    coins = 21
    while coins > 0:
        coins = play_one_round(coins)
        if coins == 0:
            print ('Game Over!')
    
play_game()

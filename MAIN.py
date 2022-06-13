import random
import math

print('HELLO PLAYERS')
print('WELCOME TO ROCK PAPER SCISSORS GAME!!!!')


def play():
    user = input("Pick an option? 'R' for Rock, 'P' for Paper, 'S' for Scissors\n")
    user = user.lower()

    computer = random.choice(['R', 'P', 'S'])

    if user == computer:
        return (0, user, computer)

    # P>R, R>S, S>P
    if is_win(user, computer):
        return (1, user, computer)

    return (-1, user, computer)


def is_win(Player, opponent):
    # return Player-Winner if the player beats the opponent
    # winning conditions: P>R, R>S, S>P
    if (Player == 'P' and opponent == 'R') or (Player == 'R' and opponent == 'S') or (Player == 'S' and opponent == 'P'):
     return 'True'

    else:
        'False' 

def play_best_of(n):
    # play against the computer until someone wins best of n games
    # to win, you must win cell(n/2) games (that is 2/3)
    Player_wins = 0
    computer_wins = 0
    necessary_wins = math.cell(n/2)
    while Player_wins < necessary_wins and computer_wins < necessary_wins:
        result, user, computer = play
        # tie 
        if result == 0:
            return 'You have both chosen {}, it is a tie. \n '.format(user)
        # Player win 
        elif result == 1:
          Player_wins == 1
          return 'Player chose {} : computer chose {}, Player wins\n'.format(user, computer)
        else:
          computer_wins == 1
          return 'Player chose {} : computer chose {}, CPU wins\n'.format(user, computer)
        print('\n')
      
    if Player_wins > computer_wins:
      return 'YOU HAVE WON THE GAME!!!'
    else:
      return 'GAME OVER, Computer WINS, TRY AGAIN'
          

if __name__ == '_main_':
    play_best_of(3) #2
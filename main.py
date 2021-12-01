# Rock paper scissors game

import random

def play():
    user = input("Whats your choice? Choose 'r' for rock, 's' for scissors or 'p' for paper: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'

    # r>s, s>p, p>r
    if is_win(user, computer):
        return 'You won!'

    return 'You looose!'

#return True if player wins
def is_win(player, opponent):
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


print(play())

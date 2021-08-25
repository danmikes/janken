import random

# moves
move = ('R','P','S')

# this bot makes random moves
def player(prev_play, opponent_history=[]):

  # generate random move
  guess = random.choice(move)

  return guess

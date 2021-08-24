import random

# moves
move = ('R','P','S')

# this bot makes random moves
def player(prev_play, opponent_history=[]):

  # generate random move
  guess = move[random.randint(0,2)]

  return guess

import random

#moves
move = ('R','P','S')

def player(prev_play, opponent_history=[]):

  # generate random move
  guess = move[random.randint(0,2)]

  return guess

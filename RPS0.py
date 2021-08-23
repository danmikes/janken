import random

def player(prev_play, opponent_history=[]):
  opponent_history.append(prev_play)

  # generate random move
  guess = move[random.randint(0,2)]

  return guess

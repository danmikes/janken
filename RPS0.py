import random

# moves
move = ('R','P','S')

# last move -> best counter move for next move
next_best = {'R':'S','P':'R','S':'P'}

# thit bot assumes opponent never makes same move twice
# chooses winning move from two remaining moves
def player(prev_play, opponent_history=[]):

  # generate random move
  guess = move[random.randint(0,2)]

  # read last move
  if prev_play != "":
    # make best counter move
    guess = next_best[prev_play]

  return guess

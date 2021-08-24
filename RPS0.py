import random

# moves
move = ('R','P','S')

# best counter move
next_best = {'R':'P','P':'S','S':'R'}

# thit bot assumes opponent never makes same move twice
# chooses winning move from two remaining moves
def player(prev_play, opponent_history=[]):
  opponent_history.append(prev_play)

  # generate random move
  guess = move[random.randint(0,2)]

  # read last move
  last_one = ""
  if len(opponent_history) >= 1:
    last_one = opponent_history[-1]
    # make best counter move
    guess = next_best[last_one]
    print(last_one)

  # print(next_mat)
  return guess

import random

# moves
move = ('R','P','S')

# last two moves
last_mat = [
  ['RR','RP','RS'],
  ['PR','PP','PS'],
  ['SR','SP','SS']
]

# best counter move
next_best = {'R':'P','P':'S','S':'R'}

# count all next for all last two ->
next_mat = [
  [[0,0,0],[0,0,0],[0,0,0]],
  [[0,0,0],[0,0,0],[0,0,0]],
  [[0,0,0],[0,0,0],[0,0,0]]
]

# add last move to last_mat and count to next_mat
def addLastTwo(prev_play, opponent_history=[]):
  last_one = ""
  if len(opponent_history) >= 1:
    last_one = opponent_history[-1]
  prev_two = ""
  # add last move to respective counter in next_mat
  if len(opponent_history) >= 3:
    prev_two = "".join(opponent_history[-3:-1])
    for i in range(3):
      for j in range(3):
        # find index of previous last two
        if last_mat[i][j] == prev_two:
          for k in range(3):
            # find index of last move
            if move[k] == last_one:
              # raise count of last move for previous last two
              next_mat[i][j][k] += 1

# predict next move from occurrence in next_mat
def predictNext(prev_play, opponent_history=[]):
  last_one = ""
  if len(opponent_history) >= 1:
    last_one = opponent_history[-1]
  # find index of last two
  else:
    last_two = ""
    if len(opponent_history) >= 2:
      last_two = "".join(opponent_history[-2:])
      for i in range(3):
        for j in range(3):
          # find index of last two
          if last_mat[i][j] == last_two:
            # find expected third move
            next_max = max(next_mat[i][j])
            if next_max == 0:
              # generate random move
              guess = move[random.randint(0,2)]
            else:
              next_index = next_mat[i][j].index(next_max)
              next_move = move[next_index]
              # make best response move
              guess = next_best[next_move]

# this bot maps all permutations (9) of two move sequences
# for each counts occurrence of third move options (3)
# predicts third move
# chooses best counter move
def player(prev_play, opponent_history=[]):
  opponent_history.append(prev_play)

  # add last two moves to last_mat
  addLastTwo(opponent_history)

  # todo: add random moves
  # ratio of naive / smart action
  beta = 0.5
  # generate choice between naive and smart action
  alpha = random.rand()
  if alpha > beta:
    # predict next move from next_mat
    smart_move
    predictNext(opponent_history)
  else:
    # generate random move
    guess = move[random.randint(0,2)]

  return guess

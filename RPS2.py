import random

# moves
move = ('R','P','S')

# last three moves
last_mat = [
  [['RRR','RRP','RRS'],
   ['RPR','RPP','RPS'],
   ['RSR','RSP','RSS']],
  [['PRR','PRP','PRS'],
   ['PPR','PPP','PPS'],
   ['PSR','PSP','PSS']],
  [['SRR','SRP','SRS'],
   ['SPR','SPP','SPS'],
   ['SSR','SSP','SSS']]
]

# best counter move
next_best = {'R':'P','P':'S','S':'R'}

# count all next for all last three ->
next_mat = [
  [[[0,0,0],[0,0,0],[0,0,0]],
   [[0,0,0],[0,0,0],[0,0,0]],
   [[0,0,0],[0,0,0],[0,0,0]]],
  [[[0,0,0],[0,0,0],[0,0,0]],
   [[0,0,0],[0,0,0],[0,0,0]],
   [[0,0,0],[0,0,0],[0,0,0]]],
  [[[0,0,0],[0,0,0],[0,0,0]],
   [[0,0,0],[0,0,0],[0,0,0]],
   [[0,0,0],[0,0,0],[0,0,0]]]
]

# add last three to last_mat
def addLastThree(opponent_history=[]):
  last_one = ""
  if len(opponent_history) >= 1:
    last_one = opponent_history[-1]
  # add last move to respective counter in next_mat
  prev_three = ""
  if len(opponent_history) >= 4:
    prev_three = "".join(opponent_history[-4:-1])
    for i in range(3):
      for j in range(3):
        for k in range(3):
          # find index of previous last three
          if last_mat[i][j][k] == prev_three:
            for l in range(3):
              # find index of last move
              if move[l] == last_one:
                # raise count of last move for previous last three
                next_mat[i][j][k][l] += 1

# predict next move from next_mat
def predictNext(opponent_history=[]):
  last_one = ""
  if len(opponent_history) >= 1:
    last_one = opponent_history[-1]
  # find index of last two
  else:
    last_three = ""
    if len(opponent_history) >= 3:
      last_three = "".join(opponent_history[-3:])
      for i in range(3):
        for j in range(3):
          for k in range(3):
            # find index of last three
            if last_mat[i][j][k] == last_three:
              # find expected fourth move
              next_max = max(next_mat[i][j][k])
              if next_max == 0:
                # generate random move
                guess = move[random.randint(0,2)]
              else:
                next_index = next_mat[i][j][k].index(next_max)
                next_move = move[next_index]
                # make best response move
                guess = next_best[next_move]

# this bot maps all permutations (27) of three move sequences
# for each counts occurrence of fourth move options (3)
# predicts next move
# choose best counter move
def player(prev_play, opponent_history=[]):
  opponent_history.append(prev_play)

  # generate random move
  guess = move[random.randint(0,2)]

  # add last three moves to last_mat
  addLastThree(opponent_history)

  # predict next move from next_mat
  predictNext(opponent_history)

  return guess

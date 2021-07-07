# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random

n = 5

def player(prev_play, opponent_history=[], play_order={}):
  
  if not prev_play:
        prev_play = 'P'
  opponent_history.append(prev_play)

  last_plays = "".join(opponent_history[-n:])
  lp_copy = last_plays[:]

  while len(lp_copy) >= 3:
    if lp_copy in play_order:
      play_order[lp_copy] += 1
    else:
      play_order[lp_copy] = 1

    lp_copy = lp_copy[1:]

  if len(opponent_history) < n:
    return random.choice(['R', 'P', 'S'])
  
  while len(last_plays) >=3:
    potential_plays = [
          last_plays[1:] +  "R",
          last_plays[1:] + "P",
          last_plays[1:] + "S",
      ]

    sub_order = {
          k: play_order[k]
          for k in potential_plays if k in play_order
      }

    try:
      prediction = max(sub_order, key=sub_order.get)[-1:]
      ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
      return ideal_response[prediction]
    except:
      last_plays = last_plays[1:]
      continue

  return random.choice(['R', 'P', 'S'])
 
pointsAwarded = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}


def part1(data):  # sourcery skip: assign-if-exp
  score = 0
  for line in data:
    bothMoves = line.split(' ')
    opponentMove = pointsAwarded[bothMoves[0]]
    yourMove = pointsAwarded[bothMoves[1]]

    if opponentMove == yourMove:
      score += yourMove + 3
      continue

    elif yourMove == 1:
      if opponentMove == 3:
        score += yourMove + 6
      else:
        score += yourMove + 0
      continue

    elif yourMove == 2:
      if opponentMove == 1:
        score += yourMove + 0
      else:
        score += yourMove + 6
      continue

    elif yourMove == 3:
      score += yourMove + 0
      continue

  return score


def part2(data):
  return None
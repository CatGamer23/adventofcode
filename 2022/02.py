translateList = {'A': "Rock", 'B': "Paper", 'C': "Scissors",
                 'X': "Rock", 'Y': "Paper", 'Z': "Scissors"}
movePoints = {"Rock": 1, "Paper": 2, "Scissors": 3}
winningMoves = {
  "Rock": "Paper",
  "Paper": "Scissors",
  "Scissors": "Rock"
}


def part1(data):  # sourcery skip: assign-if-exp
  score = 0
  for gameRound in data:
    bothMoves = gameRound.split(' ')
    opponentMove = translateList[bothMoves[0]]
    yourMove = translateList[bothMoves[1]]

    score += movePoints[yourMove]
    if opponentMove == yourMove:
      score += 3
    elif winningMoves[opponentMove] == yourMove:
      score += 6

  return score


def part2(data):
  return None
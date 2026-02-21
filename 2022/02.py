translateList: dict[str, str] = {'A': "Rock", 'B': "Paper", 'C': "Scissors", 'X': "Rock", 'Y': "Paper", 'Z': "Scissors"}
movePoints: dict[str, int] = {"Rock": 1, "Paper": 2, "Scissors": 3}
winningMoves: dict[str, str] = {"Rock": "Paper", "Paper": "Scissors", "Scissors": "Rock"}


def part1(data: list[str]) -> str | int | float | None:
  score = 0
  for gameRound in data:
    bothMoves: list[str] = gameRound.split(' ')
    opponentMove: str = translateList[bothMoves[0]]
    yourMove: str = translateList[bothMoves[1]]

    score += movePoints[yourMove]
    if opponentMove == yourMove:
      score += 3
    elif winningMoves[opponentMove] == yourMove:
      score += 6

  return score


def part2(data: list[str]) -> str | int | float | None:
  actionsList: dict[str, str] = {'X': "Lose", 'Y': "Draw", 'Z': "Win"}
  losingMoves: dict[str, str] = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}
  score = 0

  for gameRound in data:
    bothMoves: list[str] = gameRound.split(' ')
    opponentMove: str = translateList[bothMoves[0]]
    yourAction: str = actionsList[bothMoves[1]]

    if yourAction == "Draw":
      yourMove: str = opponentMove
    elif yourAction == "Lose":
      yourMove: str = losingMoves[opponentMove]
    elif yourAction == "Win":
      yourMove: str = winningMoves[opponentMove]

    score += movePoints[yourMove]
    if opponentMove == yourMove:
      score += 3
    elif winningMoves[opponentMove] == yourMove:
      score += 6

  return score
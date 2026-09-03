from main import Solution

translateList: dict[str, str] = {
  "A": "Rock",
  "B": "Paper",
  "C": "Scissors",
  "X": "Rock",
  "Y": "Paper",
  "Z": "Scissors",
}
movePoints: dict[str, int] = {"Rock": 1, "Paper": 2, "Scissors": 3}
winningMoves: dict[str, str] = {
  "Rock": "Paper",
  "Paper": "Scissors",
  "Scissors": "Rock",
}


def part1(data: list[str]) -> Solution:
  score = 0
  for gameRound in data:
    both_moves: list[str] = gameRound.split(" ")
    opponent_move: str = translateList[both_moves[0]]
    your_move: str = translateList[both_moves[1]]

    score += movePoints[your_move]
    if opponent_move == your_move:
      score += 3
    elif winningMoves[opponent_move] == your_move:
      score += 6

  return score


def part2(data: list[str]) -> Solution:
  actions_list: dict[str, str] = {"X": "Lose", "Y": "Draw", "Z": "Win"}
  losing_moves: dict[str, str] = {
    "Rock": "Scissors",
    "Paper": "Rock",
    "Scissors": "Paper",
  }
  score = 0

  for gameRound in data:
    both_moves: list[str] = gameRound.split(" ")
    opponent_move: str = translateList[both_moves[0]]
    your_action: str = actions_list[both_moves[1]]
    your_move: str = ""

    if your_action == "Draw":
      your_move: str = opponent_move
    elif your_action == "Lose":
      your_move: str = losing_moves[opponent_move]
    elif your_action == "Win":
      your_move: str = winningMoves[opponent_move]

    score += movePoints[your_move]
    if opponent_move == your_move:
      score += 3
    elif winningMoves[opponent_move] == your_move:
      score += 6

  return score

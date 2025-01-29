from rich import print

def part1(data: list[str]) -> str | int | float | None:
  moveindex = {'^': (0, 1), 'v': (0, -1), '>': (1, 0), '<': (-1, 0)}
  x, y = 0, 0
  visited = {(x, y)}

  for move in data[0]:
    x += moveindex[move][0]
    y += moveindex[move][1]
    visited.add((x, y))

  return len(visited)


def part2(data: list[str]) -> str | int | float | None:
  return None
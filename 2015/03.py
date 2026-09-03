from main import Solution


def part1(data: list[str]) -> Solution:
  lookup_table: dict[str, tuple[int, int]] = {
    "^": (0, 1),
    "v": (0, -1),
    ">": (1, 0),
    "<": (-1, 0),
  }
  x, y = 0, 0
  visited: set[tuple[int, int]] = {(x, y)}

  for direction in data[0]:
    x += lookup_table[direction][0]
    y += lookup_table[direction][1]
    visited.add((x, y))

  return len(visited)


def part2(data: list[str]) -> Solution:
  lookup_table: dict[str, tuple[int, int]] = {
    "^": (0, 1),
    "v": (0, -1),
    ">": (1, 0),
    "<": (-1, 0),
  }
  santa: tuple[int, int] = (0, 0)
  robot: tuple[int, int] = (0, 0)
  visited: set[tuple[int, int]] = {santa}

  for i, direction in enumerate(data[0]):
    if i % 2 == 0:
      santa: tuple[int, int] = (santa[0] + lookup_table[direction][0], santa[1] + lookup_table[direction][1])  # fmt: skip
      visited.add(santa)
    else:
      robot: tuple[int, int] = (robot[0] + lookup_table[direction][0], robot[1] + lookup_table[direction][1])  # fmt: skip
      visited.add(robot)

  return len(visited)

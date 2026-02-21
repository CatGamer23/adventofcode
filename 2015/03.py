def part1(data: list[str]) -> str | int | float | None:
  lookupTable: dict[str, tuple[int, int]] = {
    "^": (0, 1),
    "v": (0, -1),
    ">": (1, 0),
    "<": (-1, 0),
  }
  x, y = 0, 0
  visited: set[tuple[int, int]] = {(x, y)}

  for direction in data[0]:
    x += lookupTable[direction][0]
    y += lookupTable[direction][1]
    visited.add((x, y))

  return len(visited)


def part2(data: list[str]) -> str | int | float | None:
  lookupTable: dict[str, tuple[int, int]] = {
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
      santa: tuple[int, int] = (santa[0] + lookupTable[direction][0], santa[1] + lookupTable[direction][1])  # fmt: off
      visited.add(santa)
    else:
      robot: tuple[int, int] = (robot[0] + lookupTable[direction][0], robot[1] + lookupTable[direction][1])  # fmt: off
      visited.add(robot)

  return len(visited)

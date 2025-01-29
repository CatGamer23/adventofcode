def part1(data: list[str]) -> str | int | float | None:
  lookupTable = {'^': (0, 1), 'v': (0, -1), '>': (1, 0), '<': (-1, 0)}
  x, y = 0, 0
  visited = {(x, y)}

  for direction in data[0]:
    x += lookupTable[direction][0]
    y += lookupTable[direction][1]
    visited.add((x, y))

  return len(visited)


def part2(data: list[str]) -> str | int | float | None:
  lookupTable = {'^': (0, 1), 'v': (0, -1), '>': (1, 0), '<': (-1, 0)}
  santa = (0, 0)
  robot = (0, 0)
  visited = {santa}

  for i, direction in enumerate(data[0]):
    if i % 2 == 0:
      santa = (santa[0] + lookupTable[direction][0], santa[1] + lookupTable[direction][1])
      visited.add(santa)
    else:
      robot = (robot[0] + lookupTable[direction][0], robot[1] + lookupTable[direction][1])
      visited.add(robot)

  return len(visited)
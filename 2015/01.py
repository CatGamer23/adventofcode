def part1(data: list[str]) -> str | int | float | None:
  count = 0
  for char in data[0]:
    count += 1 if char == '(' else -1
  return count


def part2(data: list[str]) -> str | int | float | None:
  count, pos = 0, 0
  for char in data[0]:
    count += 1 if char == '(' else -1
    pos += 1
    if count <= -1:
      return pos
  return count
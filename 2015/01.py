from main import Solution


def part1(data: list[str]) -> Solution:
  count = 0
  for char in data[0]:
    count += 1 if char == "(" else -1
  return count


def part2(data: list[str]) -> Solution:
  count: int = 0
  for pos, char in enumerate(data[0], 1):
    count += 1 if char == "(" else -1
    if count <= -1:
      return pos
  return count

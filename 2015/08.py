def part1(data: list[str]) -> str | int | float | None:
  total_characters: int = 0
  total_interpreted: int = 0

  for line in data:
    total_characters += len(line)
    total_interpreted += len(line.encode("utf-8").decode("unicode_escape")) - 2

  return total_characters - total_interpreted


def part2(data: list[str]) -> str | int | float | None:
  return sum(2 + line.count("\\") + line.count('"') for line in data)

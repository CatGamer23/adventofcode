from typing import Literal


def part1(data: list[str]) -> str | int | float | None:
  priority = 0
  for line in data:
    middle_index: int = len(line) // 2
    common_items_set: set[str] = set(line[:middle_index]).intersection(
      line[middle_index:]
    )
    common_item: str = common_items_set.pop()
    ascii_start: Literal[96, 38] = 96 if common_item.islower() else 38
    priority += ord(common_item) - ascii_start
  return str(priority)


def part2(data: list[str]) -> str | int | float | None:
  groups: list[list[str]] = [
    [data[i], data[i + 1], data[i + 2]] for i, _ in enumerate(data[:-2]) if i % 3 == 0
  ]
  priority = 0
  for group in groups:
    common_items_set: set[str] = set(group[0]).intersection(group[1], group[2])
    common_item: str = common_items_set.pop()
    ascii_start: Literal[96, 38] = 96 if common_item.islower() else 38
    priority += ord(common_item) - ascii_start
  return str(priority)

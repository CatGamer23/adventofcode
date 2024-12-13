from rich import print
import itertools


def part1(data: list[str]) -> str | int | float | None:
  container_sizes: list[int] = list(map(int, data))

  valid_combinations: int = 0
  for i in range(len(container_sizes)):
    for combination in itertools.combinations(container_sizes, i):
      if sum(combination) == 150:
        valid_combinations += 1

  return valid_combinations


def part2(data: list[str]) -> str | int | float | None:
  return None
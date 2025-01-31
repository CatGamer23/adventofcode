import math


def get_divisors(number: int) -> set[int]:
  return {
    i for i in range(1, int(math.sqrt(number)) + 1)
    if number % i == 0
    for i in (i, number // i)
  }


def part1(data: list[str]) -> str | int | float | None:
  for i in range(100000, 1000000):
    if sum(get_divisors(i)) * 10 >= int(data[0]):
      return i
  return None


def part2(data: list[str]) -> str | int | float | None:
  return None
from itertools import groupby


def part1(data: list[str]) -> str | int | float | None:
  largest = 0
  reformattedData: list[list[str]] = [
    list(group) for key, group in groupby(data, key=lambda x: x == "") if not key
  ]

  for subList in reformattedData:
    total = 0
    for calorie in subList:
      total += int(calorie)
      largest: int = max(largest, total)

  return largest


def part2(data: list[str]) -> str | int | float | None:
  finaltotal = 0
  totalsList: list[int] = []
  reformattedData: list[list[str]] = [
    list(group) for key, group in groupby(data, key=lambda x: x == "") if not key
  ]

  totalsList.extend(
    sum(int(calorie) for calorie in subList) for subList in reformattedData
  )
  totalsList.sort()

  for i in totalsList[-3:]:
    finaltotal += i

  return finaltotal

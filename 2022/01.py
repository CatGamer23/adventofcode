def part1(data: list[str]) -> str | int | float | None:
  largest = 0
  from itertools import groupby
  reformattedData =  [list(group) for key, group in groupby(
    data, key=lambda x: x == '') if not key]

  for subList in reformattedData:
    total = 0
    for calorie in subList:
      total += int(calorie)
      if total > largest:
        largest = total

  return largest


def part2(data: list[str]) -> str | int | float | None:
  finaltotal = 0
  totalsList = []
  from itertools import groupby
  reformattedData =  [list(group) for key, group in groupby(
    data, key=lambda x: x == '') if not key]

  totalsList.extend(sum(int(calorie) for calorie in subList) for subList in reformattedData)
  totalsList.sort()

  for i in totalsList[-3:]:
    finaltotal += i

  return finaltotal
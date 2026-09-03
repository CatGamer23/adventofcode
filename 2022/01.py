from itertools import groupby

from main import Solution


def part1(data: list[str]) -> Solution:
  largest = 0
  reformatted_data: list[list[str]] = [
    list(group) for key, group in groupby(data, key=lambda x: x == "") if not key
  ]

  for subList in reformatted_data:
    total = 0
    for calorie in subList:
      total += int(calorie)
      largest: int = max(largest, total)

  return largest


def part2(data: list[str]) -> Solution:
  final_total = 0
  totals_list: list[int] = []
  reformatted_data: list[list[str]] = [
    list(group) for key, group in groupby(data, key=lambda x: x == "") if not key
  ]

  totals_list.extend(
    sum(int(calorie) for calorie in subList) for subList in reformatted_data
  )
  totals_list.sort()

  for i in totals_list[-3:]:
    final_total += i

  return final_total

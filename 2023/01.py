from main import Solution


def part1(data: list[str]) -> Solution :
  total = 0
  for line in data:
    num: str = "".join(char for char in line if char.isdigit())
    finalnum: str = num[0]
    finalnum += num[-1]
    total += int(finalnum)
  return total


def part2(data: list[str]) -> Solution:
  # conversionTable: dict[str, str] = {
  #   "one": "1",
  #   "two": "2",
  #   "three": "3",
  #   "four": "4",
  #   "five": "5",
  #   "six": "6",
  #   "seven": "7",
  #   "eight": "8",
  #   "nine": "9",
  # }
  # total = 0
  # for line in data:
  #   finalnum: str = ""
  #   for char in line:
  #     letter: str = "".join(char)
  #     if letter in conversionTable:
  #       finalnum += conversionTable[letter]
  #     if char.isdigit():
  #       finalnum += char
  #   print(finalnum)
  #   # total += int(finalnum[0] + finalnum[-1])
  # return total
  return None

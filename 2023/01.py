def part1(data):
  total = 0
  for line in data:
    num = ''.join(char for char in line if char.isdigit())
    finalnum = num[0]
    finalnum += num[-1]
    total += int(finalnum)
  return total


def part2(data):
  conversionTable = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
  total = 0
  # add together the spelled out numbers in the data
  for line in data:
    num = conversionTable[''.join(char for char in line if char.isalpha())]
    print(num)
  return total
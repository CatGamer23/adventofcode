def part1(data):
  total = 0
  for line in data:
    num = ''.join(char for char in line if char.isdigit())
    finalnum = num[0]
    finalnum += num[-1]
    total += int(finalnum)
  return total


def part2(data):
  return None
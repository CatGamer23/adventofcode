def part1(data):
  count, previous = 0, 0
  for i in range(len(data)):
    if int(data[i]) > previous:
      count += 1
    previous = int(data[i])
  return count - 1


def part2(data):
  return None

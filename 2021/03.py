def part1(data):
  counts = {"first": 0, "second": 0, "third": 0, "fourth": 0, "fifth": 0, "sixth": 0,
            "seventh": 0, "eighth": 0, "ninth": 0, "tenth": 0, "eleventh": 0, "twelfth": 0}
  for line in data:
    loopCount = 0
    lineList = [char for char in line]
    for char in lineList:
      if char == 1:
        counts[counts[loopCount]] += 1
      loopCount += 1
  return counts


def part2(data):
  return None

def part1(data):
  totalsList = []
  curTotal = 0
  for calorie in data:
    if calorie == '':
      totalsList.append(curTotal)
      curTotal = 0
    
    calorie = int(calorie)
    curTotal += calorie

  return max(totalsList)


def part2(data):
  return None
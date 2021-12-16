def part1(data):
  laternFishes = data[0]
  for _ in range(1):
    for fish in laternFishes.split(','):
      fish = int(fish)
      if fish == 0:
        laternFishes += ",8"
      else:
        fish -= 1
  return len(laternFishes.split(','))

def part2(data):
  return None

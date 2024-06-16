def part1(data):
  laternFishes = data[0].split(',')
  for _ in range(80):
    for i in range(len(laternFishes)):
      laternFishes[i] = int(laternFishes[i])
      if laternFishes[i] == 0:
        laternFishes[i] = 6
        laternFishes.append(8)
      else:
        laternFishes[i] -= 1
  return len(laternFishes)


def part2(data):
  laternFishes = data[0].split(',')
  for _ in range(256):
    for i in range(len(laternFishes)):
      laternFishes[i] = int(laternFishes[i])
      if laternFishes[i] == 0:
        laternFishes[i] = 6
        laternFishes.append(8)
      else:
        laternFishes[i] -= 1
  return len(laternFishes)

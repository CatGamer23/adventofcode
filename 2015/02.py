def part1(data):
  total = 0
  for line in data:
    l, w, h = map(int, line.split('x'))
    total += 2*l*w + 2*w*h + 2*h*l
    total += min(l*w, w*h, h*l)
  return total


def part2(data):
  total = 0
  for line in data:
    sizes = line.split('x')
    sizes.sort(key=int)
    l, w, h = map(int, sizes)
    total += l*w*h + 2*l + 2*w
  return total

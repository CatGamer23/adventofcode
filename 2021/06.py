from main import Solution


def part1(data: list[str]) -> Solution | None:
  lantern_fishes: list[int] = list(map(int, data[0].split(",")))
  for _ in range(80):
    for i in range(len(lantern_fishes)):
      lantern_fishes[i] = int(lantern_fishes[i])
      if lantern_fishes[i] == 0:
        lantern_fishes[i] = 6
        lantern_fishes.append(8)
      else:
        lantern_fishes[i] -= 1
  return len(lantern_fishes)


def part2(data: list[str]) -> Solution | None:
  lantern_fishes: list[int] = list(map(int, data[0].split(",")))
  for _ in range(256):
    for i in range(len(lantern_fishes)):
      lantern_fishes[i] = int(lantern_fishes[i])
      if lantern_fishes[i] == 0:
        lantern_fishes[i] = 6
        lantern_fishes.append(8)
      else:
        lantern_fishes[i] -= 1
  return len(lantern_fishes)

def part1(data: list[str]) -> str | int | float | None:
  total = 0
  for line in data:
    l, w, h = map(int, line.split("x"))
    total += 2*(l*w + w*h + h*l)  # fmt: skip
    total += min(l*w, w*h, h*l)  # fmt: skip
  return total


def part2(data: list[str]) -> str | int | float | None:
  total = 0
  for line in data:
    sizes: list[str] = line.split("x")
    sizes.sort(key=int)
    l, w, h = map(int, sizes)
    total += l*w*h + 2*l + 2*w  # fmt: skip
  return total

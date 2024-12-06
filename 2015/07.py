from rich import print


def part1(data: list[str]) -> str | int | float | None:
  # data = [
  #     '123 -> x',
  #     '456 -> y',
  #     'x AND y -> d',
  #     'x OR y -> e',
  #     'x LSHIFT 2 -> f',
  #     'y RSHIFT 2 -> g',
  #     'NOT x -> h',
  #     'NOT y -> i'
  # ]

  storage: dict[str, int] = {}

  for line in data:
    signal, wire = line.split(' -> ')
    data = signal.split(' ')

    if len(data) == 1:
      storage[wire] = int(
        data[0]) if data[0].isnumeric() else storage.get(data[0], 0)
    elif data[0] == 'NOT':
      storage[wire] = ~storage.get(data[1], 0) & 65535
    else:
      op1 = storage.get(data[0], 0)
      op2 = int(data[2]) if data[2].isnumeric() else storage.get(data[2], 0)
      if data[1] == 'AND':
        storage[wire] = op1 & op2
      elif data[1] == 'OR':
        storage[wire] = op1 | op2
      elif data[1] == 'LSHIFT':
        storage[wire] = op1 << op2
      elif data[1] == 'RSHIFT':
        storage[wire] = op1 >> op2

  print(dict(sorted(storage.items())))
  return storage['a']


def part2(data: list[str]) -> str | int | float | None:
  return None
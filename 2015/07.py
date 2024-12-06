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
    print(f"Processing line: {line}")
    signal, wire = line.split(' -> ')
    data = signal.split(' ')
    print(f"Signal: {signal}, Wire: {wire}, Data: {data}")

    if len(data) == 1:
      value = int(data[0]) if data[0].isnumeric() else storage.get(data[0], 0)
      storage[wire] = value
      print(f"Assigned {value} to {wire}")
    elif data[0] == 'NOT':
      value = ~storage.get(data[1], 0) & 65535
      storage[wire] = value
      print(f"Assigned {value} to {wire} (NOT operation)")
    else:
      op1 = storage.get(data[0], 0)
      op2 = int(data[2]) if data[2].isnumeric() else storage.get(data[2], 0)
      print(f"Operands: {op1}, {op2}")
      if data[1] == 'AND':
        value = op1 & op2
        storage[wire] = value
        print(f"Assigned {value} to {wire} (AND operation)")
      elif data[1] == 'OR':
        value = op1 | op2
        storage[wire] = value
        print(f"Assigned {value} to {wire} (OR operation)")
      elif data[1] == 'LSHIFT':
        value = op1 << op2
        storage[wire] = value
        print(f"Assigned {value} to {wire} (LSHIFT operation)")
      elif data[1] == 'RSHIFT':
        value = op1 >> op2
        storage[wire] = value
        print(f"Assigned {value} to {wire} (RSHIFT operation)")

  print("Final storage state:", dict(sorted(storage.items())))
  return storage.get('a', None)


def part2(data: list[str]) -> str | int | float | None:
  return None
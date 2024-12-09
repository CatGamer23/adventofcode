import itertools


def part1(data: list[str]) -> str | int | float | None:
  sequence = data[0]

  for _ in range(40):
    next_sequence = []
    for digit, group in itertools.groupby(sequence):
      group_length = len(list(group))
      next_sequence.append(str(group_length) + digit)
    sequence = ''.join(next_sequence)

  return len(sequence)


def part2(data: list[str]) -> str | int | float | None:
  sequence = data[0]

  for _ in range(50):
    next_sequence = []
    for digit, group in itertools.groupby(sequence):
      group_length = len(list(group))
      next_sequence.append(str(group_length) + digit)
    sequence = ''.join(next_sequence)

  return len(sequence)
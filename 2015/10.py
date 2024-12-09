import itertools

def part1(data: list[str]) -> str | int | float | None:
  expanded_input = data[0]

  for _ in range(40):
    new_expanded_input = []
    for digit, group in itertools.groupby(expanded_input):
      # print(digit, str(group))
      count = len(list(group))
      new_expanded_input.append(str(count) + digit)
    expanded_input = ''.join(new_expanded_input)

  return len(expanded_input)


def part2(data: list[str]) -> str | int | float | None:
  expanded_input = data[0]

  for _ in range(50):
    new_expanded_input = []
    for digit, group in itertools.groupby(expanded_input):
      count = len(list(group))
      new_expanded_input.append(str(count) + digit)
    expanded_input = ''.join(new_expanded_input)

  return len(expanded_input)
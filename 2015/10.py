def part1(data: list[str]) -> str | int | float | None:
  expanded_input = list(data[0])

  for _ in range(40):
    i = 0
    while i < len(expanded_input):
      count = 1
      while i + count < len(expanded_input) and expanded_input[i] == expanded_input[i + count]:
        count += 1

      expanded_input[i:i + count] = list(str(count) + expanded_input[i])
      i += len(str(count)) + 1

  return len(expanded_input)


def part2(data: list[str]) -> str | int | float | None:
  return None
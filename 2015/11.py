from string import ascii_lowercase


def from_decimal(value: int, base: int = 26) -> str:
  digits: list[str] = []
  while value > 0:
    value -= 1
    value, remainder = divmod(value, base)
    digits.append(chr(remainder + ord("a")))
  return "".join(reversed(digits))


def to_decimal(string: str, base: int = 26) -> int:
  result: int = 0
  for char in string:
    result: int = result * base + (ord(char) - ord("a") + 1)
  return result


# Rules:
# 1. It does not contain the letters i, o, or l.
# 2. It contains the straight increasing three letters.
# 3. It contains at least two different, non-overlapping pairs of letters.
def part1(data: list[str]) -> str | int | float | None:
  data_as_int: int = to_decimal(data[0])

  invalid_password: bool = True
  while invalid_password:
    data_as_int += 1
    password: str = from_decimal(data_as_int)

    # Rule 1
    if "i" in password or "o" in password or "l" in password:
      continue

    # Rule 2
    three_in_a_row: bool = any(
      password[i : i + 3] in ascii_lowercase for i in range(len(password) - 2)
    )

    if not three_in_a_row:
      continue

    # Rule 3
    pairs: int = 0
    i: int = 0
    while i < len(password) - 1:
      if password[i] == password[i + 1]:
        pairs += 1
        i += 2
      else:
        i += 1

    if pairs < 2:
      continue

    invalid_password = False
  return from_decimal(data_as_int)


def part2(data: list[str]) -> str | int | float | None:
  data_as_int: int = to_decimal(str(part1(data)))

  invalid_password: bool = True
  while invalid_password:
    data_as_int += 1
    password: str = from_decimal(data_as_int)

    # Rule 1
    if "i" in password or "o" in password or "l" in password:
      continue

    # Rule 2
    three_in_a_row: bool = any(
      password[i : i + 3] in ascii_lowercase for i in range(len(password) - 2)
    )

    if not three_in_a_row:
      continue

    # Rule 3
    pairs: int = 0
    i: int = 0
    while i < len(password) - 1:
      if password[i] == password[i + 1]:
        pairs += 1
        i += 2
      else:
        i += 1

    if pairs < 2:
      continue

    invalid_password = False
  return from_decimal(data_as_int)

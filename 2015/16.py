from rich import print


def part1(data: list[str]) -> str | int | float | None:
  cache: dict[int, dict[str, int]] = {}
  gift_sender: dict[str, int] = {
      "children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0,
      "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1
  }

  for line in data:
    _, sue_number, compound1_type, compound1, compound2_type, compound2, compound3_type, compound3 = line.replace(
      ',', '').replace(':', '').split(' ')

    cache[int(sue_number)] = {
      compound1_type: int(compound1),
      compound2_type: int(compound2),
      compound3_type: int(compound3)
    }

  for sue_num, compounds in cache.items():
    if all(compounds[key] == gift_sender[key] for key in compounds):
      return sue_num

  return "No matching Aunt Sue found"


def part2(data: list[str]) -> str | int | float | None:
  return None
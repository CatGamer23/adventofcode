def part1(data: list[str]) -> str | int | float | None:
  cache: dict[int, dict[str, int]] = {}
  gift_sender: dict[str, int] = {
      "children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0,
      "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1
  }

  for line in data:
    parts = line.replace(',', '').replace(':', '').split(' ')
    sue_number = parts[1]
    compound1, compound1_type = parts[3], parts[2]
    compound2, compound2_type = parts[5], parts[4]
    compound3, compound3_type = parts[7], parts[6]

    cache[int(sue_number)] = {
      compound1_type: int(compound1),
      compound2_type: int(compound2),
      compound3_type: int(compound3)
    }

  for sue_num, compounds in cache.items():
    if compounds.items() <= gift_sender.items():
      return sue_num

  return "No matching Aunt Sue found"


def part2(data: list[str]) -> str | int | float | None:
  cache: dict[int, dict[str, int]] = {}
  gift_sender: dict[str, int] = {
      "children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0,
      "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1
  }

  for line in data:
    parts = line.replace(',', '').replace(':', '').split(' ')
    sue_number = parts[1]
    compound1, compound1_type = parts[3], parts[2]
    compound2, compound2_type = parts[5], parts[4]
    compound3, compound3_type = parts[7], parts[6]

    cache[int(sue_number)] = {
      compound1_type: int(compound1),
      compound2_type: int(compound2),
      compound3_type: int(compound3)
    }

  for sue_num, compounds in cache.items():
    if all(
      (key in ["cats", "trees"] and compounds[key] > gift_sender[key]) or
      (key in ["pomeranians", "goldfish"] and compounds[key] < gift_sender[key]) or
      (key not in ["cats", "trees", "pomeranians", "goldfish"] and compounds[key] == gift_sender[key])
      for key in compounds
    ):
      return sue_num

  return "No matching Aunt Sue found"
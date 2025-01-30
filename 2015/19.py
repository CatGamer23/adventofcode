from rich import print


def part1(data: list[str]) -> str | int | float | None:
  replacement_rules: list[str] = data[:-2]
  starting_molecule: str = data[-1]
  unique_molecules: set[str] = set()

  for rule in replacement_rules:
    input_molecule, output_molecule = rule.split(' => ')
    for i in range(len(starting_molecule)):
      if starting_molecule.startswith(input_molecule, i):
        new_molecule: str = starting_molecule[:i] + output_molecule + starting_molecule[i + len(input_molecule):]  # noqa
        unique_molecules.add(new_molecule)

  return len(unique_molecules)


def part2(data: list[str]) -> str | int | float | None:
  return None
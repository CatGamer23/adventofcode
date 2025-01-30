def part1(data: list[str]) -> str | int | float | None:
  # *replacement_rules, _, starting_molecule = data
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
  replacement_rules: list[tuple[str, ...]] = [tuple(rule.split(' => ')[::-1]) for rule in data[:-2]]  # noqa
  molecule_goal: str = data[-1]
  steps: int = 0

  while molecule_goal != "e":
    for output_molecule, input_molecule in replacement_rules:
      if output_molecule in molecule_goal:
        molecule_goal = molecule_goal.replace(
          output_molecule, input_molecule, 1)
        steps += 1
        break

  return steps
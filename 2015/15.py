from rich import print
import itertools


def part1(data: list[str]) -> str | int | float | None:
  ingredients: dict[str, dict[str, int]] = {}

  for line in data:
    parts: list[str] = line.replace(',', '').replace(':', '').split(' ')
    name, _, capacity, _, durability, _, flavor, _, texture, _, calories = parts

    ingredients[name] = {
      'capacity': int(capacity),
      'durability': int(durability),
      'flavor': int(flavor),
      'texture': int(texture),
      'calories': int(calories)
    }


  print(ingredients)
  max_score: int = 0
  



  return None


def part2(data: list[str]) -> str | int | float | None:
  return None
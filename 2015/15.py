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

  max_score: int = 0
  for sugar_qty in range(101):
    for sprinkles_qty in range(101 - sugar_qty):
      for chocolate_qty in range(101 - sugar_qty - sprinkles_qty):
        candy_qty = 100 - sugar_qty - sprinkles_qty - chocolate_qty

        ingredient_names: list[str] = list(ingredients.keys())
        total_capacity: int = max(
            0,
            sugar_qty * ingredients[ingredient_names[0]]['capacity'] +
            sprinkles_qty * ingredients[ingredient_names[1]]['capacity'] +
            chocolate_qty * ingredients[ingredient_names[2]]['capacity'] +
            candy_qty * ingredients[ingredient_names[3]]['capacity']
        )
        total_durability: int = max(
            0,
            sugar_qty * ingredients[ingredient_names[0]]['durability'] +
            sprinkles_qty * ingredients[ingredient_names[1]]['durability'] +
            chocolate_qty * ingredients[ingredient_names[2]]['durability'] +
            candy_qty * ingredients[ingredient_names[3]]['durability']
        )
        total_flavor: int = max(
            0,
            sugar_qty * ingredients[ingredient_names[0]]['flavor'] +
            sprinkles_qty * ingredients[ingredient_names[1]]['flavor'] +
            chocolate_qty * ingredients[ingredient_names[2]]['flavor'] +
            candy_qty * ingredients[ingredient_names[3]]['flavor']
        )
        total_texture: int = max(
            0,
            sugar_qty * ingredients[ingredient_names[0]]['texture'] +
            sprinkles_qty * ingredients[ingredient_names[1]]['texture'] +
            chocolate_qty * ingredients[ingredient_names[2]]['texture'] +
            candy_qty * ingredients[ingredient_names[3]]['texture']
        )

        score: int = total_capacity * total_durability * total_flavor * total_texture

        max_score = max(max_score, score)

  return max_score


def part2(data: list[str]) -> str | int | float | None:
  return None
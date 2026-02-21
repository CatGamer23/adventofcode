from dataclasses import dataclass
from itertools import combinations, product


def part1(data: list[str]) -> str | int | float | None:
  boss_hp: int = int(data[0].split(": ")[1])
  boss_damage: int = int(data[1].split(": ")[1])
  boss_armor: int = int(data[2].split(": ")[1])
  player_hp: int = 100

  def simulate_battle(player_damage: int, player_armor: int) -> bool:
    player_turns_to_win: int = -(-boss_hp // max(1, player_damage - boss_armor))
    boss_turns_to_win: int = -(-player_hp // max(1, boss_damage - player_armor))
    return player_turns_to_win <= boss_turns_to_win

  @dataclass
  class Item:
    name: str
    cost: int
    damage: int
    armor: int

  items: list[Item] = [
    # weapons
    Item("Dagger", 8, 4, 0),
    Item("Shortsword", 10, 5, 0),
    Item("Warhammer", 25, 6, 0),
    Item("Longsword", 40, 7, 0),
    Item("Greataxe", 74, 8, 0),
    # armor
    Item("No Armor", 0, 0, 0),
    Item("Leather", 13, 0, 1),
    Item("Chainmail", 31, 0, 2),
    Item("Splintmail", 53, 0, 3),
    Item("Bandedmail", 75, 0, 4),
    # rings
    Item("No Ring", 0, 0, 0),
    Item("Damage +1", 25, 1, 0),
    Item("Damage +2", 50, 2, 0),
    Item("Damage +3", 100, 3, 0),
    Item("Defense +1", 20, 0, 1),
    Item("Defense +2", 40, 0, 2),
    Item("Defense +3", 80, 0, 3),
  ]

  min_cost: float = float("inf")
  for weapon, armor, (ring1, ring2) in product(
    items[:5], items[5:10], combinations(items[10:], 2)
  ):
    cost: int = weapon.cost + armor.cost + ring1.cost + ring2.cost
    damage: int = weapon.damage + ring1.damage + ring2.damage
    armor_value: int = armor.armor + ring1.armor + ring2.armor
    if simulate_battle(damage, armor_value):
      min_cost: float = min(min_cost, cost)

  return min_cost


def part2(data: list[str]) -> str | int | float | None:
  boss_hp: int = int(data[0].split(": ")[1])
  boss_damage: int = int(data[1].split(": ")[1])
  boss_armor: int = int(data[2].split(": ")[1])
  player_hp: int = 100

  def simulate_battle(player_damage: int, player_armor: int) -> bool:
    player_turns_to_win: int = -(-boss_hp // max(1, player_damage - boss_armor))
    boss_turns_to_win: int = -(-player_hp // max(1, boss_damage - player_armor))
    return player_turns_to_win > boss_turns_to_win

  @dataclass
  class Item:
    name: str
    cost: int
    damage: int
    armor: int

  items: list[Item] = [
    # weapons
    Item("Dagger", 8, 4, 0),
    Item("Shortsword", 10, 5, 0),
    Item("Warhammer", 25, 6, 0),
    Item("Longsword", 40, 7, 0),
    Item("Greataxe", 74, 8, 0),
    # armor
    Item("No Armor", 0, 0, 0),
    Item("Leather", 13, 0, 1),
    Item("Chainmail", 31, 0, 2),
    Item("Splintmail", 53, 0, 3),
    Item("Bandedmail", 75, 0, 4),
    # rings
    Item("No Ring", 0, 0, 0),
    Item("Damage +1", 25, 1, 0),
    Item("Damage +2", 50, 2, 0),
    Item("Damage +3", 100, 3, 0),
    Item("Defense +1", 20, 0, 1),
    Item("Defense +2", 40, 0, 2),
    Item("Defense +3", 80, 0, 3),
  ]

  max_cost: float = float("-inf")
  for weapon, armor, (ring1, ring2) in product(
    items[:5], items[5:10], combinations(items[10:], 2)
  ):
    cost: int = weapon.cost + armor.cost + ring1.cost + ring2.cost
    damage: int = weapon.damage + ring1.damage + ring2.damage
    armor_value: int = armor.armor + ring1.armor + ring2.armor
    if simulate_battle(damage, armor_value):
      max_cost: float = max(max_cost, cost)

  return max_cost

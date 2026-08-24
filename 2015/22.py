from dataclasses import dataclass


@dataclass
class Item:
  name: str
  cost: int
  damage: int
  armor: int
  heal: int
  duration: int


items: list[Item] = [
  # Spells
  Item("Magic Missile", 53, 4, 0, 0, 0),
  Item("Drain", 73, 2, 0, 2, 0),

  # Effects
  Item("Shield", 113, 0, 7, 0, 6),
  Item("Poison", 173, 3, 0, 0, 6),
  Item("Recharge", 229, 0, 0, 101, 5),
]

def part1(data: list[str]) -> str | int | float | None:
  boss_hp: int = int(data[0].split(": ")[1])
  boss_damage: int = int(data[1].split(": ")[1])
  player_hp: int = 50
  player_mana: int = 500

  def simulate_battle(player_damage: int, player_mana: int) -> bool:
    # Apply effects
    # Effect duration -1, if duration = 0, remove effect
    # effect applies
    # Boss attacks

    return True

  return None


def part2(data: list[str]) -> str | int | float | None:
  return None

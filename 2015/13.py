import itertools


def part1(data: list[str]) -> str | int | float | None:
  people_cache: dict[str, dict[str, int]] = {}

  for line in data:
    person1: str
    gain_or_lose: str
    amount: str
    person2: str
    person1, _, gain_or_lose, amount, _, _, _, _, _, _, person2 = line.replace('.', '').split(' ')  # fmt: skip

    # Convert the amount to an integer and make it negative if the person is losing happiness
    calculated_amount: int = int(amount) if gain_or_lose == "gain" else -int(amount)  # noqa

    # Add the person to the cache if they don't exist, along with the other person and the amount of happiness
    people_cache.setdefault(person1, {})[person2] = calculated_amount

  biggest_change: int = 0
  for perm in itertools.permutations(people_cache.keys()):
    happiness: int = 0
    for i in range(len(perm)):
      happiness += people_cache[perm[i]][perm[(i + 1) % len(perm)]]
      happiness += people_cache[perm[i]][perm[(i - 1) % len(perm)]]
    biggest_change: int = max(biggest_change, happiness)

  return biggest_change


def part2(data: list[str]) -> str | int | float | None:
  people_cache: dict[str, dict[str, int]] = {"Me": {}}

  for line in data:
    person1: str
    gain_or_lose: str
    amount: str
    person2: str
    person1, _, gain_or_lose, amount, _, _, _, _, _, _, person2 = line.replace('.', '').split(' ')  # fmt: skip

    # Add person to the 'Me' cache with a happiness of 0
    people_cache["Me"][person1] = 0

    # Convert the amount to an integer and make it negative if the person is losing happiness
    calculated_amount: int = int(amount) if gain_or_lose == "gain" else -int(amount)

    # Add the person to the cache if they don't exist, along with the other person and the amount of happiness
    people_cache.setdefault(person1, {"Me": 0})[person2] = calculated_amount

  biggest_change: int = 0
  for perm in itertools.permutations(people_cache.keys()):
    happiness: int = 0
    for i in range(len(perm)):
      happiness += people_cache[perm[i]][perm[(i + 1) % len(perm)]]
      happiness += people_cache[perm[i]][perm[(i - 1) % len(perm)]]
    biggest_change: int = max(biggest_change, happiness)

  return biggest_change

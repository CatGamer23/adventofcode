from rich import print
import itertools


def part1(data: list[str]) -> str | int | float | None:
  shortest_distance: float = float('inf')
  route_distances: set[int] = set()
  cities: set[str] = set()
  distances: dict[tuple[str, str], int] = {}

  # Each line: city1 to city2 = distance
  for line in data:
    parts = line.split(' ')
    city1: str = parts[0]
    city2: str = parts[2]
    distance: int = int(parts[4])

    distances[(city1, city2)] = distance
    distances[(city2, city1)] = distance

    cities.add(city1)
    cities.add(city2)

  for route in itertools.permutations(cities):
    total_distance: int = 0
    for i in range(len(route) - 1):
      total_distance += distances[(route[i], route[i + 1])]
    route_distances.add(total_distance)

  shortest_distance = min(route_distances)

  return shortest_distance


def part2(data: list[str]) -> str | int | float | None:
  shortest_distance: float = float('inf')
  route_distances: set[int] = set()
  cities: set[str] = set()
  distances: dict[tuple[str, str], int] = {}

  # Each line: city1 to city2 = distance
  for line in data:
    parts = line.split(' ')
    city1: str = parts[0]
    city2: str = parts[2]
    distance: int = int(parts[4])

    distances[(city1, city2)] = distance
    distances[(city2, city1)] = distance

    cities.add(city1)
    cities.add(city2)

  for route in itertools.permutations(cities):
    total_distance: int = 0
    for i in range(len(route) - 1):
      total_distance += distances[(route[i], route[i + 1])]
    route_distances.add(total_distance)

  shortest_distance = max(route_distances)

  return shortest_distance
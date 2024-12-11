from rich import print


def part1(data: list[str]) -> str | int | float | None:
  computed_data: dict[str, dict[str, int]] = {}

  for line in data:
    parts = line.split()
    reindeer = parts[0]
    speed = int(parts[3])
    fly_time = int(parts[6])
    rest_time = int(parts[13])

    computed_data[reindeer] = {
      'speed': speed,
      'fly_time': fly_time,
      'rest_time': rest_time,
      'distance_per_cycle': speed * fly_time,
      'cycle_time': fly_time + rest_time
    }

  furthest_distance: int = 0
  for reindeer, stats in computed_data.items():
    cycle_time = stats['cycle_time']
    distance_per_cycle = stats['distance_per_cycle']
    speed = stats['speed']
    fly_time = stats['fly_time']

    full_cycles, remaining_time = divmod(2503, cycle_time)
    distance = full_cycles * distance_per_cycle + min(remaining_time, fly_time) * speed  # noqa

    furthest_distance = max(furthest_distance, distance)

  return furthest_distance


def part2(data: list[str]) -> str | int | float | None:
  return None
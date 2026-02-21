def part1(data: list[str]) -> str | int | float | None:
  computed_data: dict[str, dict[str, int]] = {}

  for line in data:
    parts: list[str] = line.split()
    reindeer: str = parts[0]
    speed = int(parts[3])
    fly_time = int(parts[6])
    rest_time = int(parts[13])

    computed_data[reindeer] = {
      "speed": speed,
      "fly_time": fly_time,
      "rest_time": rest_time,
      "distance_per_cycle": speed * fly_time,
      "cycle_time": fly_time + rest_time,
    }

  furthest_distance: int = 0
  for reindeer, stats in computed_data.items():
    cycle_time: int = stats["cycle_time"]
    distance_per_cycle: int = stats["distance_per_cycle"]
    speed: int = stats["speed"]
    fly_time: int = stats["fly_time"]

    full_cycles, remaining_time = divmod(2503, cycle_time)
    distance: int = (
      full_cycles * distance_per_cycle + min(remaining_time, fly_time) * speed
    )

    furthest_distance: int = max(furthest_distance, distance)

  return furthest_distance


def part2(data: list[str]) -> str | int | float | None:
  computed_data: dict[str, dict[str, int]] = {}

  for line in data:
    parts: list[str] = line.split()
    reindeer: str = parts[0]
    speed = int(parts[3])
    fly_time = int(parts[6])
    rest_time = int(parts[13])

    computed_data[reindeer] = {
      "speed": speed,
      "fly_time": fly_time,
      "rest_time": rest_time,
      "distance_per_cycle": speed * fly_time,
      "cycle_time": fly_time + rest_time,
      "points": 0,
    }

  # Simulate the race and add a point to the leading reindeer per second
  for second in range(2503):
    for reindeer, stats in computed_data.items():
      cycle_time: int = stats["cycle_time"]
      distance_per_cycle: int = stats["distance_per_cycle"]
      speed: int = stats["speed"]
      fly_time: int = stats["fly_time"]

      full_cycles, remaining_time = divmod(second, cycle_time)
      distance: int = (
        full_cycles * distance_per_cycle + min(remaining_time, fly_time) * speed
      )

      stats["current_distance"] = distance

    leading_reindeer: str = max(
      computed_data, key=lambda r: computed_data[r]["current_distance"]
    )
    computed_data[leading_reindeer]["points"] += 1

  return max(computed_data[reindeer]["points"] for reindeer in computed_data) - 1

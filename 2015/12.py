import json
from typing import Any


def find_numbers(obj: Any, ignored_value: str | None = None) -> int:
  if isinstance(obj, int):
    return obj
  if isinstance(obj, list):
    return sum(find_numbers(elem, ignored_value) for elem in obj)
  if isinstance(obj, dict):
    if ignored_value in obj.values():
      return 0
    return sum(find_numbers(val, ignored_value) for val in obj.values())
  return 0


def part1(data: list[str]) -> str | int | float | None:
  parsed_json_data: Any = json.loads("".join(data))

  # Recursively search for numbers
  return find_numbers(parsed_json_data)


def part2(data: list[str]) -> str | int | float | None:
  parsed_json_data: Any = json.loads("".join(data))

  # Recursively search for numbers, ignoring the property "red"
  return find_numbers(parsed_json_data, "red")

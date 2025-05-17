import json
from typing import Any


def find_numbers(obj: Any, ignored_property: str | None = None) -> int:
  if isinstance(obj, int):
    return obj
  if isinstance(obj, list):
    return sum(find_numbers(i, ignored_property) for i in obj)  # type: ignore
  if isinstance(obj, dict):
    if ignored_property in obj.values():
      return 0
    return sum(find_numbers(i, ignored_property) for i in obj.values())  # type: ignore
  return 0


def part1(data: list[str]) -> str | int | float | None:
  parsed_json_data: dict[str, Any] = json.loads(''.join(data))

  # Recursively search for numbers
  return find_numbers(parsed_json_data)


def part2(data: list[str]) -> str | int | float | None:
  parsed_json_data: dict[str, Any] = json.loads(''.join(data))

  # Recursively search for numbers, ignoring the property "red"
  return find_numbers(parsed_json_data, "red")
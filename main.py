#!/usr/bin/env uv run

import argparse
import datetime
import importlib
import itertools
import os
import subprocess
import time
from collections.abc import Callable
from stat import S_IREAD
from types import ModuleType

import requests
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Parse command line arguments
parser = argparse.ArgumentParser(description="Run Advent of Code challenges.")
parser.add_argument(
  "-d", "--day", type=int, help="Specify the day of the challenge (1-25)."
)
parser.add_argument(
  "-y",
  "--year",
  type=int,
  help="Specify the year of the challenge (2015-current).",
)
parser.add_argument(
  "-s",
  "--setup",
  action="store_true",
  help="Set up the directory structure and files.",
)
args: argparse.Namespace = parser.parse_args()

# Set global variables
type Solution = str | int | float | None
current_year: int = datetime.datetime.now(tz=datetime.UTC).year
session_cookie: str | None = os.getenv(key="AOC_COOKIE")
input_url = "https://adventofcode.com/{}/day/{}/input"
default_code_template = """from main import Solution


def part1(data: list[str]) -> Solution:
    return None

def part2(data: list[str]) -> Solution:
    return None"""


# Format time in a human-readable format
def format_time(ms: float) -> str:
  if ms < 0.01:  # < 10 microseconds (Immediately terminated)
    return "N/A"
  elif ms < 1:  # < 1 millisecond (microseconds)
    return f"{round(ms * 1000):.0f}µs"
  elif ms < 1000:  # < 1 second (milliseconds)
    return f"{round(ms)}ms"
  elif ms < 60000:  # < 1 minute (seconds)
    return f"{round(ms / 1000, 2)}s"
  elif ms < 3600000:  # < 1 hour (minutes and seconds)
    minutes, seconds = divmod(ms / 1000, 60)
    return f"{int(minutes)}m {seconds:.2f}s"
  else:  # >= 1 hour
    return "You took way too long to solve this problem..."


# Run specific part for a given day and year
def run_part(part_number: int, module: ModuleType, input_data: list[str]) -> float:
  part_function = getattr(module, f"part{part_number}", None)

  if not callable(part_function):
    print(f"No part{part_number} function")
    return 0.0

  print(f"Running Part {part_number}")
  start_time: float = time.perf_counter()
  result: Solution = part_function(input_data)
  end_time: float = time.perf_counter()

  print(f"Output: {result}")
  execution_time: float = (end_time - start_time) * 1000  # sec -> ms
  print(f"Took: {format_time(execution_time)}")
  return execution_time


# Get input data
def get_input_data(day_padded: str, year: int) -> list[str]:
  input_file_path = f"./{year}/Inputs/Day {day_padded} Input.txt"

  with open(input_file_path, "r") as input_file:
    data_lines: list[str] = [line.rstrip() for line in input_file]

  return data_lines


# Execute the challenge for the selected day and year
def execute_challenge(day_padded: str, year: int) -> None:
  print(f"AoC {year} - Day {day_padded}\n")

  module: ModuleType = importlib.import_module(name=f"{year}.{day_padded}")
  input_data: list[str] = get_input_data(day_padded, year)

  part1_time: float = run_part(1, module, input_data)
  part2_time: float = run_part(2, module, input_data)
  total_time: float = part1_time + part2_time

  print(f"Total runtime: {format_time(total_time)}")


# region File Structure Setup
# Pull input file for user from AoC
def download_input_file(year: int, day: int, input_file: str) -> None:
  if session_cookie is None:
    raise ValueError("Session cookie is not set")

  response = requests.get(
    input_url.format(year, day), cookies={"session": session_cookie}
  )

  if response.status_code == 404:
    raise ConnectionRefusedError(f"Day {day}, {year} is locked")

  if response.text.startswith("<!DOCTYPE html>"):
    raise ValueError("Invalid session cookie or captcha required")

  with open(input_file, "w") as file:
    file.write(response.text.rstrip())

  os.chmod(input_file, S_IREAD)


# Create a file with default code template if it does not exist
def create_file_if_not_exists(file_path: str) -> None:
  if not os.path.exists(file_path):
    with open(file_path, "w") as file:
      file.write(default_code_template)


# Set up the directory structure and files
def setup() -> None:
  for setup_year, setup_day in itertools.product(
    range(2015, current_year), range(1, 26)
  ):
    day_padded = str(setup_day).zfill(2)

    day_file = f"./{setup_year}/{day_padded}.py"
    input_file = f"./{setup_year}/Inputs/Day {day_padded} Input.txt"

    os.makedirs(f"{setup_year}/Inputs/", exist_ok=True)
    create_file_if_not_exists(day_file)

    if not os.path.exists(input_file):
      download_input_file(setup_year, setup_day, input_file)


# endregion File Structure Setup


if __name__ == "__main__":
  if args.setup:
    setup()
  else:
    year: int = args.year or current_year
    day: int = args.day or int(input("Day: ").strip())

    try:
      if not (1 <= day <= 25):
        raise ValueError("Day must be a number between 1 and 25")

      subprocess.run(["clear"], check=False)
      execute_challenge(str(day).zfill(2), year)

    except KeyboardInterrupt:
      print("\nExiting...")

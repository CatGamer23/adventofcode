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

current_year: int = datetime.datetime.now(tz=datetime.UTC).year

# Parse command line arguments
parser = argparse.ArgumentParser(description="Run Advent of Code challenges.")
parser.add_argument(
  "-d", "--day", type=int, help="Specify the day of the challenge (1-25)."
)
parser.add_argument(
  "-y",
  "--year",
  type=int,
  default=current_year,
  help="Specify the year of the challenge (2015-current).",
)
parser.add_argument(
  "-s",
  "--setup",
  type=bool,
  action="store_true",
  help="Set up the directory structure and files.",
)
args = parser.parse_args()

# Type alias for the expected signature of any AoC solver function
type Solution = str | int | float | None
type Solver = Callable[[list[str]], Solution]

# Set global variables
session_cookie: str | None = os.getenv(key="AOC_COOKIE")
input_url = "https://adventofcode.com/{}/day/{}/input"
default_code_template = """def part1(data: list[str]) -> Solution:
    return None

def part2(data: list[str]) -> Solution:
    return None"""


# Format execution time in a human-readable format
def format_executiontime(milliseconds: float) -> str:
  if milliseconds < 1:  # < 1 millisecond (microseconds)
    return f"{round(milliseconds * 1000)}µs"
  elif milliseconds < 1000:  # < 1 second (milliseconds)
    return f"{round(milliseconds)}ms"
  elif milliseconds < 60000:  # < 1 minute (seconds)
    return f"{round(milliseconds / 1000, 2)}s"
  elif milliseconds < 3600000:  # < 1 hour (minutes and seconds)
    minutes, seconds = divmod(milliseconds / 1000, 60)
    return f"{int(minutes)}m {round(seconds, 2)}s"
  else:  # >= 1 hour
    return "You took way too long to solve this problem..."


# Run specific part for a given day and year
def run_part(
  part_number: int, module: ModuleType, input_data: list[str]
) -> float | None:
  part_function = getattr(module, f"part{part_number}", None)
  if not callable(part_function):
    print(f"No part{part_number} function")
    return None

  print(f"Running Part {part_number}")
  start_time = time.perf_counter()
  result: Solution = part_function(input_data)
  end_time = time.perf_counter()

  print(f"Output: {result}")
  execution_time = (end_time - start_time) * 1000  # sec -> ms
  print(f"Took {format_executiontime(milliseconds=execution_time)}\n")
  return execution_time


# Get input data
def get_input_data(day_padded: str, year: int) -> list[str]:
  input_file_path = f"./{year}/Inputs/Day {day_padded} Input.txt"
  try:
    with open(file=input_file_path, mode="r") as input_file:
      data_lines = [line.rstrip() for line in input_file]
  except Exception as error:
    raise PermissionError(f"Unable to read file {input_file_path}") from error

  return data_lines


# Execute the challenge for the selected day and year
def execute_challenge(day_padded: str, year: int):
  print(f"AoC {year} - Day {day_padded}\n")

  module: ModuleType = importlib.import_module(name=f"{year}.{day_padded}")
  input_data = get_input_data(day_padded, year)

  part1_time: float = run_part(part_number=1, module=module, input_data=input_data) or 0
  part2_time: float = run_part(part_number=2, module=module, input_data=input_data) or 0
  total_time: float = part1_time + part2_time
  print(
    f"Total runtime: {format_executiontime(milliseconds=total_time) if total_time else 'N/A'}"
  )


# Run the challenge for the selected year
def run(selected_year: int | None = None, selected_day: int | None = None):
  year = selected_year or args.year
  day = selected_day or args.day or int(input("Day: ").strip())

  try:
    if not (1 <= day <= 25):
      raise ValueError("Day must be a number between 1 and 25")

    subprocess.run(
      args="cls" if os.name == "nt" else ["clear"], shell=True, check=False
    )
    execute_challenge(day_padded=str(day).zfill(2), year=year)

  except KeyboardInterrupt:
    print("\nExiting...")

  except Exception as error:
    raise RuntimeError(f"An error occurred: {type(error).__name__}: {error}") from error


# Create a file with default code template if it does not exist
def create_file_if_not_exists(file_path: str):
  if not os.path.exists(file_path):
    with open(file=file_path, mode="w") as file:
      file.write(default_code_template)


# Download the input file for a given day and year
def download_input_file(year: int, day: int, input_file: str):
  if session_cookie is None:
    raise ValueError("Session cookie is not set")

  response = requests.get(
    input_url.format(year, day), cookies={"session": session_cookie}
  )

  if response.status_code == 404:
    raise ConnectionRefusedError(f"Day {day}, {year} is locked")

  if response.text.startswith("<!DOCTYPE html>"):
    raise ValueError("Invalid session cookie or captcha required")

  with open(input_file, mode="w") as file:
    file.write(response.text.rstrip())

  os.chmod(path=input_file, mode=S_IREAD)


# Set up the directory structure and files
def setup():
  for year, day in itertools.product(range(2015, current_year), range(1, 26)):
    day_padded = str(day).zfill(2)

    day_file = f"./{year}/{day_padded}.py"
    input_file = f"./{year}/Inputs/Day {day_padded} Input.txt"

    os.makedirs(name=f"./{year}/Inputs/", exist_ok=True)

    create_file_if_not_exists(file_path=day_file)

    if not os.path.exists(path=input_file):
      try:
        download_input_file(year, day, input_file)
      except ConnectionRefusedError as e:
        print(e)
        break


# ------------------------ RUN CODE BELOW ------------------------
if __name__ == "__main__":
  subprocess.run(args="cls" if os.name == "nt" else ["clear"], shell=True, check=False)
  if args.setup:
    setup()
  else:
    run()

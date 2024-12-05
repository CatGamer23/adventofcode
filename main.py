# RUN AT END OF FILE, NOT HERE
import datetime
import itertools
import math
import os
import sys
import time
from stat import S_IREAD

import requests
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

session_cookie: str | None = os.getenv('AOC_COOKIE')
input_url: str = "https://adventofcode.com/{}/day/{}/input"  # .format(year, day) # noqa
current_year: int = datetime.datetime.now().year
default_code_template: str = """def part1(data: list[str]) -> str | int | float | None:
  return None


def part2(data: list[str]) -> str | int | float | None:
  return None"""


# Format execution time in a human-readable format
def format_executiontime(milliseconds: int | float) -> str:
  if milliseconds < 1:
    return f"{round(milliseconds * 1000)}µs"
  elif milliseconds < 1000:
    return f"{round(milliseconds)}ms"
  elif milliseconds < 60000:
    return f"{round(milliseconds / 1000, 2)}s"
  else:
    minutes = math.floor(milliseconds / 60000)
    seconds = (milliseconds % 60000) / 1000
    return f"{minutes}m {round(seconds, 2)}s"


# Run specific part for a given day and year
def run_part(part_number: int, module: str, input_data: list[str]) -> float | None:
  part_function = getattr(module, f"part{part_number}", None)
  if not callable(part_function):
    print(f"No part{part_number} function")
    return None

  print(f"Running Part {part_number}")
  start_time: float = time.perf_counter()
  result: str | int | float | None = part_function(input_data)
  end_time: float = time.perf_counter()

  print(f"Output: {result}")
  execution_time: float = (end_time - start_time) * 1000  # sec -> ms
  print(f"Took {format_executiontime(execution_time)}\n")
  return execution_time


# Get input data
def get_input_data(day: str, year: int) -> list[str]:
  input_file_path: str = f'./{year}/Inputs/Day {day} Input.txt'
  try:
    with open(input_file_path, 'r') as input_file:
      data_lines: list[str] = [line.strip() for line in input_file]
  except Exception as error:
    raise PermissionError(f"Unable to read file {input_file_path}") from error

  # print(f"Loaded puzzle input from {input_file_path}\n")
  return data_lines


# Execute the challenge for the selected day and year
def execute(day_padded: str, year: int) -> None:
  print(f"AOC {year} - Day {day_padded}\n")

  module = __import__('importlib').import_module(f'{year}.{day_padded}')
  input_data: list[str] = get_input_data(day_padded, year)

  part1_time: float = run_part(1, module, input_data) or 0
  part2_time: float = run_part(2, module, input_data) or 0
  total_time: float = part1_time + part2_time
  print(f"Total runtime: {format_executiontime(total_time) if total_time else 'N/A'}")  # noqa


# Run the challenge for the selected year
def run(selected_year: int = current_year) -> None:
  try:
    selected_day: str = (sys.argv[1] if len(
      sys.argv) > 1 else input("Day: ")).zfill(2)
    if not selected_day.isdigit() or not 1 <= int(selected_day) <= 25:
      raise ValueError("Day must be an number between 1 and 25")

    os.system('cls' if os.name == 'nt' else 'clear')
    execute(selected_day, selected_year)

  except KeyboardInterrupt:
    print("\nExiting...")

  except Exception as error:
    raise RuntimeError(f"Error: {error}") from error


# Create a file with default code template if it does not exist
def create_file_if_not_exists(file_path: str) -> None:
  if not os.path.exists(file_path):
    with open(file_path, 'w') as file:
      file.write(default_code_template)


# Download the input file for a given day and year
def download_input_file(year: int, day: str, input_file: str) -> None:
  if session_cookie is None:
    raise ValueError("Session cookie is not set")

  response = requests.get(input_url.format(year, day), cookies={
      "session": session_cookie
  })

  if response.status_code == 404:
    raise ConnectionRefusedError(f"Day {day}, {year} is locked")

  if response.text.startswith("<!DOCTYPE html>"):
    raise ValueError("Invalid session cookie or captcha required")

  with open(input_file, 'w') as file:
    file.write(response.text)

  os.chmod(input_file, S_IREAD)


# Set up the directory structure and files
def setup() -> None:
  """
  Sets up the directory structure and files for Advent of Code challenges from 2015 to the current year.
  This function performs the following steps:
    1. Iterates over each year from 2015 to the current year and each day from 1 to 25.
    2. Creates directories for each year and for input files if they do not already exist.
    3. Creates a Python file for each day if it does not already exist, writing default code into it.
    4. Downloads the input file for each day from the Advent of Code website if it does not already exist.
    5. Sets the input file to read-only.
  Note:
    - The function assumes the existence of global variables: `current_year`, `default_code_template`, `input_url`, and `session_cookie`.
    - The function uses the `requests` library to download input files and `os` library for file and directory operations.
    - If the input file for a specific day is locked (HTTP 404), the function will print a message and stop processing further days for that year.
  Raises:
    - Any exceptions raised by `requests.get` or file operations are not explicitly handled within this function.
  """
  for year, day in itertools.product(range(2015, current_year + 1), range(1, 26)):
    day_padded = str(day).zfill(2)

    day_file = f'./{year}/{day_padded}.py'
    input_file = f'./{year}/Inputs/Day {day_padded} Input.txt'

    os.makedirs(f'./{year}/Inputs/', exist_ok=True)

    create_file_if_not_exists(day_file)

    if not os.path.exists(input_file):
      download_input_file(year, day_padded, input_file)


# ------------------------ RUN CODE BELOW ------------------------
if __name__ == "__main__":
  os.system('cls' if os.name == 'nt' else 'clear')
  # setup()
  # run(int(sys.argv[1] if len(sys.argv) > 1 else input("Year: ")))
  run(2015)
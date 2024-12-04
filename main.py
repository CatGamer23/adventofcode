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

load_dotenv()

session_cookie: str | None = os.getenv('AOC_COOKIE')
input_url: str = "https://adventofcode.com/{}/day/{}/input"  # .format(year, day) # noqa
current_year: int = datetime.datetime.now().year
default_code: str = """def part1(data: list[str]) -> str | int | float | None:
  return None


def part2(data: list[str]) -> str | int | float | None:
  return None"""


def format_runtime(milliseconds: int | float) -> str:
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
  print(f"Took {format_runtime(execution_time)}\n")
  return execution_time


def get_input_data(day: str, year: int) -> list[str]:
  # Try to find the filename
  input_file_path: str = f'./{year}/Inputs/Day {day} Input.txt'
  try:
    with open(input_file_path) as input_file:
      data_lines: list[str] = [line.strip() for line in input_file]
  except Exception as error:
    raise BaseException(f"Unable to read file {input_file_path}") from error

  # print(f"Loaded puzzle input from {input_file_path}\n")
  print()
  return data_lines


def execute(day: str, year: int) -> None:
  day_padded: str = day.zfill(2)
  print(f"AOC {year} - Day {day_padded}")

  module = __import__('importlib').import_module(f'{year}.{day_padded}')
  input_data: list[str] = get_input_data(day_padded, year)

  part1_time: float = run_part(1, module, input_data) or 0
  part2_time: float = run_part(2, module, input_data) or 0
  total_time: float = part1_time + part2_time
  print(f"Total runtime: {format_runtime(total_time) if total_time else 'N/A'}")  # noqa


def run(selected_year: int = current_year) -> None:
  try:
    selected_day: str = input("Day: ") if len(sys.argv) <= 1 else sys.argv[1]
    if not selected_day.isdigit() or not 1 <= int(selected_day) <= 25:
      raise ValueError("Day must be an number between 1 and 25")

    os.system('cls' if os.name == 'nt' else 'clear')
    execute(selected_day.zfill(2), selected_year)

  except KeyboardInterrupt:
    print("\nExiting...")

  except Exception as error:
    print(f"Error: {error}")


def setup() -> None:
  for year, day in itertools.product(range(2015, current_year + 1), range(1, 26)):
    day = str(day).zfill(2)  # type: ignore

    if not os.path.exists(f'./{year}/'):
      os.mkdir(f'./{year}/')
    if not os.path.exists(f'./{year}/Inputs/'):
      os.mkdir(f'./{year}/Inputs/')

    if not os.path.exists(f'./{year}/{day}.py'):
      with open(f'./{year}/{day}.py', 'w') as f:
        f.write(default_code)

    if not os.path.exists(f'./{year}/Inputs/Day {day} Input.txt'):
      inputReq = requests.get(input_url.format(year, int(day)), cookies={
          "session": f'{session_cookie}'
      })

      if inputReq.status_code == 404:
        print(f"Dec {day}, {year} is locked")
        break

      with open(f'./{year}/Inputs/Day {day} Input.txt', 'w') as f:
        f.write(inputReq.text)
        f.close()

      os.chmod(f'./{year}/Inputs/Day {day} Input.txt', S_IREAD)


# ------------------------ RUN CODE BELOW ------------------------
if __name__ == "__main__":
  os.system('cls' if os.name == 'nt' else 'clear')
  # setup()
  # run(int(sys.argv[1] if len(sys.argv) > 1 else input("Year: ")))
  run(2015)
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

cookieValue: str | None = os.getenv('AOC_COOKIE')
url: str = "https://adventofcode.com/{}/day/{}/input"  # .format(year, day)
thisYear: int = int(datetime.date.today().strftime('%Y'))
initText: str = """def part1(data: list[str]) -> str | int | float | None:
  return None


def part2(data: list[str]) -> str | int | float | None:
  return None"""


def format_runtime(ms: int | float) -> str:
  if ms < 1:
    return f"{round(ms * 1000)}µs"
  elif ms < 1000:
    return f"{round(ms)}ms"
  elif ms < 60000:
    return f"{round(ms / 1000, 2)}s"
  else:
    minutes = math.floor(ms / 60000)
    seconds = (ms % 60000) / 1000
    return f"{minutes}m {round(seconds, 2)}s"


def run_part(part: int, mod: str, data: list[str]) -> float | None:
  func = getattr(mod, f"part{part}", None)
  if not callable(func):
    print(f"No part{part} function")
    return None

  print(f"Running Part {part}")
  start: float = time.perf_counter()
  returned_value: str | int | float | None = func(data)
  end: float = time.perf_counter()

  print(f"Output: {returned_value}")
  execution_time: float = (end - start) * 1000  # sec -> ms
  print(f"Took {format_runtime(execution_time)}\n")
  return execution_time


def get_data(day: str, year: int) -> list[str]:
  # Try to find the filename
  input_file_path: str = f'./{year}/Inputs/Day {day} Input.txt'
  try:
    with open(input_file_path) as f:
      data: list[str] = [line.strip() for line in f]
  except Exception as e:
    raise BaseException(f"Unable to read file {input_file_path}") from e

  # print(f"Loaded puzzle input from {input_file_path}\n")
  print()
  return data


def execute(day: str, year: int) -> None:
  day_padded: str = day.zfill(2)
  print(f"AOC {year} - Day {day_padded}")

  module = __import__('importlib').import_module(f'{year}.{day_padded}')
  data: list[str] = get_data(day_padded, year)

  part1_time: float | None = run_part(1, module, data)
  part2_time: float | None = run_part(2, module, data)
  if part1_time is not None and part2_time is not None:
    print(f"Total runtime: {format_runtime(part1_time + part2_time)}")
  else:
    print("Total runtime: N/A")


def run(year: int = thisYear) -> None:
  try:
    # day = sys.argv[2] if len(sys.argv) > 2 else input("Day: ")
    day = sys.argv[1] if len(sys.argv) > 1 else input("Day: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    if int(day) > 25 or int(day) <= 0:
      raise ValueError("Day must be an integer between 1 and 25")
    execute(day, year)

  except KeyboardInterrupt:
    print("\nExiting...")

  except Exception as e:
    print("Error:", e)


def setup() -> None:
  for year, day in itertools.product(range(2015, thisYear + 1), range(1, 26)):
    day = str(day).zfill(2)  # type: ignore

    if not os.path.exists(f'./{year}/'):
      os.mkdir(f'./{year}/')
    if not os.path.exists(f'./{year}/Inputs/'):
      os.mkdir(f'./{year}/Inputs/')

    if not os.path.exists(f'./{year}/{day}.py'):
      with open(f'./{year}/{day}.py', 'w') as f:
        f.write(initText)

    if not os.path.exists(f'./{year}/Inputs/Day {day} Input.txt'):
      inputReq = requests.get(url.format(year, int(day)), cookies={
          "session": f'{cookieValue}'
      })

      if inputReq.status_code == 404:
        print(f"Dec {day}, {year} is locked")
        break

      with open(f'./{year}/Inputs/Day {day} Input.txt', 'w') as f:
        f.write(inputReq.text)
        f.close()

      os.chmod(f'./{year}/Inputs/Day {day} Input.txt', S_IREAD)


# ------------------------ RUN CODE BELOW ------------------------
os.system('cls' if os.name == 'nt' else 'clear')
# setup()
# run(int(sys.argv[1] if len(sys.argv) > 1 else input("Year: ")))
run(2015)
# RUN AT END OF FILE, NOT HERE
import itertools
import sys
import time
import math
import requests
import os
import datetime
from dotenv import load_dotenv
from stat import S_IREAD
load_dotenv()

cookieValue = os.getenv('AOC_COOKIE')
url = "https://adventofcode.com/{}/day/{}/input"  # .format(year, day)
thisYear = int(datetime.date.today().strftime('%Y'))
initText = """def part1(data):
  return None


def part2(data):
  return None"""


def format_runtime(ms: int | float) -> str:
  # Microseconds
  if ms <= 1:
    return f"{round(ms * 1000)}µs"
  # Milliseconds
  if ms < 1000:
    whole_ms = math.floor(ms)
    rem_ms = ms - whole_ms
    return f"{whole_ms}ms {format_runtime(rem_ms)}"
  sec = ms / 1000
  # Seconds
  if sec < 60:
    whole_sec = math.floor(sec)
    rem_ms = ms - whole_sec * 1000
    return f'{whole_sec}s {format_runtime(rem_ms)}'
  # Minutes
  return f"{math.floor(sec / 60)}m {format_runtime(sec % 60 * 1000)}"


def run_part(part: int, mod: str, data: list[str]) -> int | float:
  funcname = f'part{part}'

  f = getattr(mod, funcname, None)
  if callable(f):
    print(f"Running Part {part}")

    start = time.perf_counter()
    val = f(data)
    end = time.perf_counter()

    print(f"Output: {val}")
    rtime = (end - start) * 1000  # sec -> ms
    print(f"Took {format_runtime(rtime)}\n")
    return rtime
  else:
    print(f"No {funcname} function")
    return 0


def get_data(day: str, year: int) -> list[str]:
  # Try to find the filename
  fname = f'./{year}/Inputs/Day {day} Input.txt'
  try:
    with open(fname) as f:
      data = f.readlines()
      data = [line.strip() for line in data]
  except Exception as e:
    raise ValueError(f"Unable to read file {fname}") from e

  # print(f"Loaded puzzle input from {fname}\n")
  print()
  return data


def execute(day: str, year: int) -> None:
  day = day.zfill(2)
  print(f"AOC {year} - Day {day}")

  mod = __import__('importlib').import_module(f'{year}.{day}')
  data = get_data(day, year)

  part1Time = run_part(1, mod, data)
  part2Time = run_part(2, mod, data)
  if part1Time != 0 and part2Time != 0:
    print(f"Total runtime: {format_runtime(part1Time + part2Time)}")


def run(year: int = thisYear) -> None:
  try:
    # day = sys.argv[2] if len(sys.argv) > 2 else input("Day: ")
    day = sys.argv[1] if len(sys.argv) > 1 else input("Day: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    if int(day) > 25 or int(day) <= 0:
      raise Exception("Day must be an integer from 1 to 25")
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
run()
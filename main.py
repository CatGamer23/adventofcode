# RUN AT END OF FILE, NOT HERE
import itertools
import time
import math
import requests
import os

cookieValue = "53616c7465645f5f191c4e9ee5de5bd7fc9d188696b2c9e72bb00e28e72e62ee08c0fe6083be3c305733060f080ff2a02ef369ee7ac904d077368caa53854802"
url = "https://adventofcode.com/{}/day/{}/input"  # .format(year, day)
thisYear = int(__import__('datetime').date.today().strftime('%Y'))
initText = """def part1(data):
  return None


def part2(data):
  return None
"""


def format_runtime(ms):
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


def run_part(part: str, mod: str, data: str):
  # sourcery skip: extract-method, remove-unnecessary-else
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


def get_data(day: int, year: int):
  # Try to find the filename
  fname = f'./{year}/Inputs/Day {day} Input.txt'
  try:
    with open(fname) as f:
      data = f.readlines()
      data = [line.strip() for line in data]
  except Exception as e:
    raise ValueError(f"Unable to read file {fname}") from e

  print(f"Loaded puzzle input from {fname}\n")
  return data


def run(year: int = thisYear):
  try:
    day = input("Day: ")
    if int(day) <= 25:
      execute(day, year)

  except ValueError:
    print("Day must be an integer from 1 to 25")

  except KeyboardInterrupt:
    print("Exiting...")


def execute(day: int, year: int):
  day = str(day).zfill(2)
  print(f"AOC {year} - Day: {day}")

  mod = __import__('importlib').import_module(f'{year}.{day}')
  data = get_data(day, year)

  part1Time = run_part(1, mod, data)
  part2Time = run_part(2, mod, data)
  if part1Time != 0 and part2Time != 0:
    print(f"Total runtime: {format_runtime(part1Time + part2Time)}")


def setup():
  for year, day in itertools.product(range(2015, thisYear), range(1, 26)):
    day = str(day).zfill(2)

    if not os.path.exists(f'./{year}/'):
      os.mkdir(f'./{year}/')
    if not os.path.exists(f'./{year}/Inputs/'):
      os.mkdir(f'./{year}/Inputs/')

    if not os.path.exists(f'./{year}/{day}.py'):
      with open(f'./{year}/{day}.py', 'w') as f:
        f.write(initText)

    # if not os.path.exists(f'./{year}/Inputs/Day {day} Input.txt'):
    inputReq = requests.get(url.format(year, day.strip("0")), cookies={
                            "session": cookieValue
                          })

    if inputReq.status_code == 404:
      print(f"Dec {day}, {year} is locked")
      break

    with open(f'./{year}/Inputs/Day {day} Input.txt', 'w') as f:
      f.write(inputReq.text)
      f.close()


# ------------------------ RUN CODE BELOW ------------------------
os.system('cls' if os.name == 'nt' else 'clear')
setup()
# run(2022)
# RUN AT END OF FILE, NOT HERE
import time
import math

cookieValue = "53616c7465645f5ff382402f79ee918526143b743435f7c90123eb1ba52a9b706ec2b764658621673156e368b44dac0f"
url = "https://adventofcode.com/{}/day/{}/"  # .format(year, day)
thisYear = int(__import__('datetime').date.today().strftime('%Y'))
initText = \
"""
def part1(data):
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
    return f"{whole_ms}ms " + format_runtime(rem_ms)
  sec = ms / 1000
  # Seconds
  if sec < 60:
    whole_sec = math.floor(sec)
    rem_ms = ms - whole_sec * 1000
    return f'{whole_sec}s ' + format_runtime(rem_ms)
  # Minutes
  return f"{math.floor(sec / 60)}m " + format_runtime((sec % 60) * 1000)


def run_part(part: str, mod: str, data: str):
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


def get_data(day, year):
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


def run(day, year=thisYear):
  day = str(day).zfill(2)
  print(f"AOC {year} - Day: {day}")

  mod = __import__('importlib').import_module(f'{year}.{day}')
  data = get_data(day, year)

  part1Time = run_part(1, mod, data)
  part2Time = run_part(2, mod, data)
  if part1Time != 0 and part2Time != 0:
    print(f"Total runtime: {format_runtime(part1Time + part2Time)}")


def setup():
  # for year in range(2015, thisYear + 1):
  year = 2021
  for day in range(1, 26):
    with open(f'./{year}/{day}.py', 'w') as f:
      f.write(initText)
    # print(f"Setting up {year} - Day {day}")
    # print(url.format(year, day))


# ------------------------ RUN CODE BELOW ------------------------
# run(1)
setup()
run(1)

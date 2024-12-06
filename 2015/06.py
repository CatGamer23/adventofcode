import numpy as np


def part1(data: list[str]) -> str | int | float | None:
  grid: np.ndarray = np.zeros((1000, 1000), dtype=int)

  for line in data:
    command: list[str] = line.split(' ')
    action: str = command[1] if command[0] == 'turn' else 'toggle'
    start: tuple[int, ...] = tuple(map(int, command[-3].split(',')))
    end: tuple[int, ...] = tuple(map(int, command[-1].split(',')))

    if action == 'on':
      grid[start[0]:end[0] + 1, start[1]:end[1] + 1] = 1
    elif action == 'off':
      grid[start[0]:end[0] + 1, start[1]:end[1] + 1] = 0
    elif action == 'toggle':
      grid[start[0]:end[0] + 1, start[1]:end[1] + 1] ^= 1

  return np.sum(grid)


def part2(data: list[str]) -> str | int | float | None:
  grid: np.ndarray = np.zeros((1000, 1000), dtype=int)

  for line in data:
    command: list[str] = line.split(' ')
    action: str = command[1] if command[0] == 'turn' else 'toggle'
    start: tuple[int, ...] = tuple(map(int, command[-3].split(',')))
    end: tuple[int, ...] = tuple(map(int, command[-1].split(',')))

    if action == 'on':
      grid[start[0]:end[0] + 1, start[1]:end[1] + 1] += 1
    elif action == 'off':
      grid[start[0]:end[0] + 1, start[1]:end[1] + 1] -= 1
      grid[grid < 0] = 0
    elif action == 'toggle':
      grid[start[0]:end[0] + 1, start[1]:end[1] + 1] += 2

  return np.sum(grid)
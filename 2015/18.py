from typing import Any

import numpy as np

from main import Solution


def part1(data: list[str]) -> Solution:
  grid: np.ndarray[Any, np.dtype[np.int32]] = np.array(
    [[char == "#" for char in row] for row in data], dtype=np.int32
  )

  for _ in range(100):
    next_grid: np.ndarray[Any, np.dtype[np.int32]] = np.zeros_like(grid)
    for row in range(grid.shape[0]):
      for col in range(grid.shape[1]):
        active_neighbors: int = (
          grid[max(0, row - 1) : row + 2, max(0, col - 1) : col + 2].sum()
          - grid[row, col]
        )
        if (
          grid[row, col] == 1
          and active_neighbors in (2, 3)
          or grid[row, col] == 0
          and active_neighbors == 3
        ):
          next_grid[row, col] = 1
    grid: np.ndarray[tuple[Any, ...], np.dtype[np.int32]] = next_grid

  return int(grid.sum())


def part2(data: list[str]) -> Solution:
  grid: np.ndarray[Any, np.dtype[np.int32]] = np.array(
    [[char == "#" for char in row] for row in data], dtype=np.int32
  )

  for _ in range(100):
    next_grid: np.ndarray[Any, np.dtype[np.int32]] = np.zeros_like(grid)
    for row in range(grid.shape[0]):
      for col in range(grid.shape[1]):
        active_neighbors: int = (
          grid[max(0, row - 1) : row + 2, max(0, col - 1) : col + 2].sum()
          - grid[row, col]
        )
        if (
          grid[row, col] == 1
          and active_neighbors in (2, 3)
          or grid[row, col] == 0
          and active_neighbors == 3
        ):
          next_grid[row, col] = 1

    next_grid[0, 0] = 1
    next_grid[0, -1] = 1
    next_grid[-1, 0] = 1
    next_grid[-1, -1] = 1
    grid: np.ndarray[tuple[Any, ...], np.dtype[np.int32]] = next_grid

  return int(grid.sum())

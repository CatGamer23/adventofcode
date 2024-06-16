import re


def part1(data):
  count = 0
  for line in data:
    if (re.search(r'.*([aeiou].*){3}', line) and re.search(r'(.)\1', line) and not re.search(r'(ab|cd|pq|xy)', line)):
      count += 1
  return count


def part2(data):
  return None

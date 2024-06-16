import hashlib


def part1(data):
  count = 0
  while True:
    md5_hash = hashlib.md5((data[0] + str(count)).encode('utf-8')).hexdigest()
    if md5_hash.startswith('00000'):
      break
    count += 1
  return count


def part2(data):
  count = 0
  while True:
    md5_hash = hashlib.md5((data[0] + str(count)).encode('utf-8')).hexdigest()
    if md5_hash.startswith('000000'):
      break
    count += 1
  return count

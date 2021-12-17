def part1(data):
  count = 1
  for line in data:
    if ['a', 'e', 'i', 'o', 'u'] in line:
      if ['ab', 'cd', 'pq', 'xy'] not in line:
        if ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz'] in line:
          count += 1
  return count


def part2(data):
  return None

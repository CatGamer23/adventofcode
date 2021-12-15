def part1(data):
  pos, depth = 0, 0
  for instruction in data:
    if instruction.startswith('forward'):
      pos += int(instruction.split(' ')[1])
    elif instruction.startswith('up'):
      depth -= int(instruction.split(' ')[1])
    elif instruction.startswith('down'):
      depth += int(instruction.split(' ')[1])
  return pos * depth


def part2(data):
  pos, depth, aim = 0, 0, 0
  for instruction in data:
    if instruction.startswith('forward'):
      pos += int(instruction.split(' ')[1])
      depth += aim * int(instruction.split(' ')[1])
    elif instruction.startswith('up'):
      aim -= int(instruction.split(' ')[1])
    elif instruction.startswith('down'):
      aim += int(instruction.split(' ')[1])
  return pos * depth

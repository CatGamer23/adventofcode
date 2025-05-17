def eval_expr(instructions: dict[str, tuple[str, ...]], wire: str, cache: dict[str, int]) -> int:
  if wire.isdigit():
    return int(wire)

  if wire in cache:
    return cache[wire]

  expression: tuple[str, ...] = instructions[wire]

  # If the expression is a single wire/number, evaluate it directly
  if len(expression) == 1:
    result: int = eval_expr(instructions, expression[0], cache)

  # If the expression is a NOT operation, evaluate the operand and apply bitwise NOT
  elif len(expression) == 2:
    result = ~eval_expr(instructions, expression[1], cache)

  # Evaluate the left and right operands
  else:
    left: int = eval_expr(instructions, expression[0], cache)
    right: int = eval_expr(instructions, expression[2], cache)

    # Apply the appropriate bitwise operation based upon operator
    if expression[1] == "AND":
      result = left & right
    elif expression[1] == "OR":
      result = left | right
    elif expression[1] == "LSHIFT":
      result = left << right
    elif expression[1] == "RSHIFT":
      result = left >> right
    else:
      raise ValueError(f"Unknown operator: {expression[1]}")

  cache[wire] = result
  return result


def part1(data: list[str]) -> str | int | float | None:
  instructions: dict[str, tuple[str, ...]] = {
    line.split(' -> ')[1]: tuple(line.split(' -> ')[0].split())
    for line in data
  }

  return eval_expr(instructions, 'a', {})


def part2(data: list[str]) -> str | int | float | None:
  # Now, take the signal you got on wire a, override wire b to that signal,
  # and reset the other wires (including wire a). What new signal is ultimately provided to wire a?
  instructions: dict[str, tuple[str, ...]] = {
    line.split(' -> ')[1]: tuple(line.split(' -> ')[0].split())
    for line in data
  }

  signal_a: int = eval_expr(instructions, 'a', {})
  instructions['b'] = (str(signal_a),)

  return eval_expr(instructions, 'a', {})
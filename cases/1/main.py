#!/usr/bin/env python3
# vim: sw=2 ts=2 et

import math
import re
import types
from typing import NamedTuple

# The closest you can get to C structs in Python
class Operation(NamedTuple):
  name: str
  usage: str
  vars: dict
  out_var: str
  func: types.FunctionType

var_prompt = "{var} = "

# List of aliases/bindings
# Usage and UI are created based on this
operation_index = {
  "+": 0,
  "add": 0,
  "-": 1,
  "sub": 1,
  "*": 2,
  "mul": 2,
  "/": 3,
  ":": 3,
  "div": 3,
  "^": 4,
  "**": 4,
  "pow": 4,
  "!": 5,
  "fac": 5,
  "gam": 5,
  "q": -1,
  "quit": -1,
}

# Operations
operations = [
  Operation(
    "Addition",
    "a + b = c",
    {'a': float, 'b': float},
    'c',
    lambda x: x['a'] + x['b']
  ),
  Operation(
    "Subtraction",
    "a - b = c",
    {'a': float, 'b': float},
    'c',
    lambda x: x['a'] - x['b']
  ),
  Operation(
    "Multiplication",
    "a * b = c",
    {'a': float, 'b': float},
    'c',
    lambda x: x['a'] * x['b']
  ),
  Operation(
    "Division",
    "a / b = c",
    {'a': float, 'b': float},
    'c',
    lambda x: x['a'] / x['b']
  ),
  Operation(
    "Exponentiation",
    "a ^ b = c",
    {'a': float, 'b': float},
    'c',
    lambda x: x['a']**x['b']
  ),
  Operation(
    "Factorial",
    "a! = b",
    {'a': float},
    'b',
    lambda x: math.gamma(x['a']+1)
  ),
  # Always last in operation list
  Operation(
    "Quit",
    "This is jank",
    None,
    '',
    None
  ),
]

def remove_ansi(string):
  ansi_regex = re.compile(r"\x1b\[[0-9;]*m")
  return ansi_regex.sub("", string)

def generate_textbox(title, body, minlength=0):
  # Remove ANSI codes for length calculations
  raw_title = remove_ansi(title)
  raw_body = [ remove_ansi(line) for line in body ]

  # Get longest line in box or minlength
  length = max(minlength, len(raw_title), max(len(line) for line in raw_body))

  # Make sure title can be centered
  length += abs(length % 2 - len(raw_title) % 2)
  title_pad = ' '*((length-len(raw_title))//2)

  # Format each body line from raw length
  formatted_body = '\n'.join([ "| {line}{line_pad} |".format(
    line_pad=' '*(length-len(raw_body[i])),
    line=body[i]
  ) for i in range(len(body)) ])

  return '''{eq}
| {title_pad}{title}{title_pad} |
|{dash}|
{body}
{eq}'''.format(eq='='*(length+4), title_pad=title_pad, title=title, dash='-'*(length+2), body=formatted_body, length=length)

def execute_oper(oper):
  print(generate_textbox(
    title="\x1b[1m{0}\x1b[m".format(oper.name),
    body=oper.usage.split('\n')
  ))

  vars_dict = dict()
  for var, type_func in oper.vars.items():
    while True:
      try:
        val = input(var_prompt.format(var=var))
        vars_dict[var] = type_func(val)
        break
      except ValueError:
        print("Invalid value: '{0}'".format(val))

  out = oper.func(vars_dict)
  print(var_prompt.format(var=oper.out_var) + str(out))
  input("Press ENTER to continue...")

def main():
  # Jank way to format aliases to operations
  aliases = dict()
  for alias, id in operation_index.items():
    alias = "\x1b[4m{0}\x1b[m".format(alias)
    if id in aliases:
      aliases[id].append(alias)
    else:
      aliases[id] = [alias]

  body = []
  for id, alias in aliases.items():
    body.append("<{key}> {name}".format(key='|'.join(alias), name=operations[id].name))

  while True:
    print(generate_textbox(
      title="\x1b[1mUsage:\x1b[m",
      body=body
    ))

    while True:
      oper_index = input(var_prompt.format(var="oper"))
      try:
        oper_id = operation_index[oper_index]
        oper = operations[oper_id]
        break
      except KeyError:
        print("Invalid operation: '{0}'".format(oper_index))

    # Jank way to exit without extra functionality
    if oper_id < 0:
      break
    execute_oper(oper)

if __name__ == "__main__":
  main()

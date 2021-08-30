#!/usr/bin/env python3

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

operation_index = {
  "+": 0,
  "add": 0
}

# Classes 
operations = [
  Operation(
    "Addition",
    "a + b = c",
    {'a': float, 'b': float},
    'c',
    lambda x: x['a'] + x['b']
  )
]

def generate_textbox(title, body, minlength=0):
  # Get longest line in box or minlength
  length = max(minlength, len(title), max(len(line) for line in body))

  formatted_body = '\n'.join([ "| {line: <{length}} |".format(line=line, length=length) for line in body ])

  return '''{eq}
| {title: <{length}} |
|{dash}|
{body}
{eq}'''.format(eq='='*(length+4), title=title, dash='-'*(length+2), body=formatted_body, length=length)

def execute_oper(oper):
  print(generate_textbox(
    title=oper.name,
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

def main():
  # Jank way to format aliases to operations
  aliases = dict()
  for alias, id in operation_index.items():
    if id in aliases:
      aliases[id].append(alias)
    else:
      aliases[id] = [alias]

  body = []
  for id, alias in aliases.items():
    body.append("<{key}> {name}".format(key='|'.join(alias), name=operations[id].name))

  while True:
    print(generate_textbox(
      title="Usage:",
      body=body
    ))

    while True:
      oper_index = input(var_prompt.format(var="oper"))
      try:
        oper = operations[operation_index[oper_index]]
        break
      except KeyError:
        print("Invalid operation: '{0}'".format(oper_index))

    execute_oper(oper)
    break

if __name__ == "__main__":
  main()

# vim: sw=2 ts=2 et

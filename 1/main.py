#!/usr/bin/env python3

usage = '''\
==========================
| Operations:            |
|------------------------|
| <+|add> addition       |
| <-|sub> subtraction    |
| <*|mul> multiplication |
| </|div> division       |
==========================\
'''

oper_usage = '''\
==========================
| {name: <23}|
|------------------------|
| {usage: <23}|
==========================\
'''

var_prompt = "{var} = "

operation_index = {
  "+": 0,
  "add": 0
}

operations = [
  {
    "name": "Addition",
    "usage": "a + b = c",
    "vars": {
      'a': float,
      'b': float
    },
    "out_var": "c",
    "func": lambda x: x['a']+x['b']
  }
]

def execute_oper(oper):
  print(oper_usage.format(
    name=oper["name"],
    usage=oper["usage"]
  ))

  vars_dict = dict()
  for var, type_func in oper["vars"].items():
    while True:
      try:
        val = input(var_prompt.format(var=var))
        vars_dict[var] = type_func(val)
        break
      except ValueError:
        print("Invalid value: '{0}'".format(val))

  out = oper["func"](vars_dict)
  print(var_prompt.format(var=oper["out_var"]) + str(out))

def main():
  while True:
    print(usage)

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

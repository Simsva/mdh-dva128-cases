#!/usr/bin/env python3
import os
import math, cmath

def cls():
  # This seems really jank but apparently most people do it
  os.system("cls" if os.name == "nt" else "clear")

def inputVar(name, type_fn):
  while 1:
    try:
      return type_fn(input("({type_name}) {name} = ".format(name=name, type_name=type_fn.__name__)))
    except ValueError as e:
      print("ERROR: Expected '{0}'".format(type_fn.__name__))

def main():
  operators = {
    "add":   { "desc": "a + b = c",     "func": lambda: inputVar('a', float) + inputVar('b', float) },
    "sub":   { "desc": "a - b = c",     "func": lambda: inputVar('a', float) - inputVar('b', float) },
    "mul":   { "desc": "a * b = c",     "func": lambda: inputVar('a', float) * inputVar('b', float) },
    "div":   { "desc": "a / b = c",     "func": lambda: inputVar('a', float) / inputVar('b', float) },
    "erfc":  { "desc": "erfc(x) = c",   "func": lambda: math.erfc(inputVar('x', float)) },
    "erf":   { "desc": "erf(x) = c",    "func": lambda: math.erf(inputVar('x', float)) },
    "lgam":  { "desc": "lgamma(x) = c", "func": lambda: math.lgamma(inputVar('x', float)) },
    "asinh": { "desc": "asinh(x) = c",  "func": lambda: cmath.asinh(inputVar('x', complex)) }
  }

  # Operator list is hardcoded
  oper_help = """\
****************************************
          Mathlete Calculator
----------------------------------------
 add   | Add two numbers
 sub   | Subtract two numbers
 mul   | Multiply two numbers
 div   | Divide two numbers
 erf   | Calculate the error function at x
 erfc  | Calculate the complementary error function at x
 lgam  | Calculate the natural logarithm of the absolute value of the Gamma function at x
 asinh | Calculate the inverse hyperbolic sine of x
----------------------------------------"""

  # Variable names are hard-coded
  usage = """\
----------------------------------------
Calculating 'c' for expression:

    {desc}
"""

  while 1:
    cls()
    print(oper_help)

    oper_name = input("Selection > ")
    if oper_name in operators:
      oper = operators[oper_name]
      print(usage.format(desc=oper["desc"]))

      print("\nRESULT: c = {}\n".format(oper["func"]()))
    else:
      print("ERROR: Unknown command '{}'".format(oper_name))

    input("Press enter to continue...")

if __name__ == "__main__":
  main()

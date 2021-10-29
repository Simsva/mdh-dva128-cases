#!/usr/bin/env python3

import math
import sys

def main():
    constants = {
        "e": math.e,
        "i": "sqrt(-1)",
        "pi": math.pi,
    }

    print("""\
--------------------------
{title:^25}
--------------------------
e    | Euler's number
i    | Imaginary unit
pi   | Archimede's constant
quit | Quit
--------------------------""".format(title="Constants"))

    while True:
        inp = input("> ")
        if inp == "quit":
            sys.exit()
        elif inp in constants:
            print(constants[inp])
        else:
            sys.stderr.write("ERROR: Unknown constant: '{}'\n".format(inp))

if __name__ == '__main__':
    main()

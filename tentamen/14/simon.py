#!/usr/bin/env python3

# Literally the same as 13

import os, sys

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    menu = """\
--------------------------
{title:^25}
--------------------------""".format(title="MathGenius")

    while True:
        cls()
        print(menu)

        s = []
        while True:
            try:
                inp = int(input("> "))
                s.append(inp)

                if inp == 0:
                    break
            except ValueError:
                sys.stderr.write("ERROR: Invalid integer\n")

        print('-'*25)
        print(f"The maximum value of the\ninput is {max(s)}")
        print('-'*25)

        input("Press ENTER to play again...")

if __name__ == '__main__':
    main()

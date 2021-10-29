#!/usr/bin/env python3

import os, sys

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    menu = """\
--------------------------
{title:^25}
--------------------------""".format(title="SuperSum")

    while True:
        cls()
        print(menu)

        s = 0
        while True:
            try:
                inp = int(input("> "))
                s += inp

                if inp == 0:
                    break
            except ValueError:
                sys.stderr.write("ERROR: Invalid integer\n")

        print('-'*25)
        print(f"The sum of the inputted\nvalues is {s}")
        print('-'*25)

        input("Press ENTER to play again...")

if __name__ == '__main__':
    main()

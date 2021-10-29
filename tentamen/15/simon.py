#!/usr/bin/env python3

# Literally the same as 13 and 14

import os, sys

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    menu = """\
--------------------------
{title:^25}
--------------------------""".format(title="Mean Mathematician")

    while True:
        cls()
        print(menu)

        s = []
        while True:
            try:
                inp = int(input("> "))
                if inp == 0:
                    break

                s.append(inp)
            except ValueError:
                sys.stderr.write("ERROR: Invalid integer\n")

        print('-'*25)
        print(f"The mean of the inputted\nvalues is {sum(s)/len(s)}")
        print('-'*25)

        input("Press ENTER to play again...")

if __name__ == '__main__':
    main()

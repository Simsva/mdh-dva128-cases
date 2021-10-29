#!/usr/bin/env python3

import os, sys
import random

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    menu = """\
--------------------------
{title:^25}
--------------------------
  Guess a number between
         0 and 99
--------------------------""".format(title="Higher Lower")

    while True:
        cls()
        print(menu)

        c = 0
        num = random.randint(0, 100)

        while True:
            try:
                guess = int(input("> "))
                c += 1

                if guess > num:
                    print("Lower!")
                elif guess < num:
                    print("Higher!")
                else:
                    print('-'*25)
                    print(f"{num} is correct!\nIt took you {c} guesses.")
                    print('-'*25)

                    input("Press ENTER to play again...")
                    break
            except ValueError:
                sys.stderr.write("ERROR: Invalid guess")

if __name__ == '__main__':
    main()

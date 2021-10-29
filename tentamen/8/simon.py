#!/usr/bin/env python3

import os, sys
import re

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    current_text = "*searching*"
    current_num = 0

    num_regex = re.compile("^[A-Za-z]{3}[0-9]{3}$")

    menu = """\
--------------------------
{title:^25}
--------------------------
{num:^25}
--------------------------"""

    while True:
        cls()
        print(menu.format(title="PlateSpotter", num=current_text))

        num_text = input("> ")

        if num_regex.match(num_text):
            num = int(num_text[3:6])

            if num == current_num+1:
                if num == 999:
                    print("The End")
                    sys.exit()
                else:
                    current_text = num_text.upper()
                    current_num = num
        else:
            sys.stderr.write(f"ERROR: Invalid plate number: '{num_text}'\n")
            input("Press ENTER to continue...")

if __name__ == '__main__':
    main()

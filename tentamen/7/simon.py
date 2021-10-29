#!/usr/bin/env python3

import os, sys

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def draw_sq(h):
    w = 2*h
    sq = (('#'*w) + '\n') * h
    print(sq, end='')

def draw_tr(h):
    w = 2*h - 1
    tr = ""
    for i in range(1, h+1):
        tr += ('#'*(2*i - 1)).center(w) + '\n'

    print(tr, end='')

def main():
    oper_help = """\
--------------------------
{title:^25}
--------------------------
sq | Draw a square
tr | Draw a triangle
q  | Quit
--------------------------""".format(title="Crazy Shapes")

    operations = {
        "sq": draw_sq,
        "tr": draw_tr,
    }

    while True:
        cls()
        print(oper_help)

        oper = input("Selection > ").lower()
        if oper == "q":
            # Special operation
            sys.exit()
        elif oper in operations:
            # Get height
            while True:
                try:
                    h = int(input("Height = "))
                    if 0<h<10:
                        break
                except ValueError:
                    # Silence exception
                    pass

                sys.stderr.write("ERROR: Invalid height\n")

            # Draw shape using height
            print('-'*25 + '\n')
            operations[oper](h)
            print('\n' + '-'*25)
        else:
            sys.stderr.write("ERROR: No such command: '{}'\n".format(oper))

        input("Press ENTER to continue...")

if __name__ == '__main__':
    main()

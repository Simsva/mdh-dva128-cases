#!/usr/bin/env python3

import os
import random

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    text = """\
|/\/\/\/\/\*/\/\/\/\/\|
|*********************|
| SUPER CRASH JACKPOT |
| MEGA CANDY TREASURE |
|---------------------|
|    -------------    |
|    | {a} | {b} | {c} |    |
|    -------------    |
|{msg:^21}|
|    CREDITS: {credits:<8}|
|---------------------|"""

    a, b, c = 0, 0, 0
    msg = "..."
    credits = 1000

    while True:
        cls()
        print(text.format(a=a, b=b, c=c, msg=msg, credits=credits))

        input("<BET>")

        a, b, c = [ random.randint(0, 9) for _ in range(3) ]

        if a == b and b == c:
            msg = "JACKPOT!"
            credits += 44
        elif a == c or b == c:
            msg = "PAIR!"
            credits += 2
        else:
            msg = "..."
            credits -= 1

        if credits == 0:
            print("You lose!")
            break

if __name__ == '__main__':
    main()

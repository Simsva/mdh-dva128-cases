#!/usr/bin/env python3

import os, sys
import random
import time

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    player = 0
    dealer = 0

    oper_help = """\
--------------------------
{title:^25}
--------------------------
hit  | Throw dice
hold | No more throws
quit | Quit the game
--------------------------""".format(title="Blackjack")

    print(oper_help)
    while True:
        oper = input(f"{player} > ")
        if oper == "hit":
            player += random.randint(1, 12)

        elif oper == "hold":
            print('-'*25)

            while dealer < 17:
                dealer += random.randint(1, 12)
                print(f"Dealer: {dealer}")

                if dealer > player:
                    break

                time.sleep(1)

            print('-'*25)

            if dealer > 21 or player > dealer:
                print("Player won")
            elif dealer > player:
                print("Dealer won")
            else:
                print("Draw")

            break

        elif oper == "quit":
            sys.exit(0)

        else:
            sys.stderr.write(f"ERROR: No such command: '{oper}'\n")

        if player > 21:
            print("Dealer won")
            break

        # input("Press ENTER to continue...")

if __name__ == '__main__':
    main()

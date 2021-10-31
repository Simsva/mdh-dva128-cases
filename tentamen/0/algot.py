#!/usr/bin/env python3
import os, time, random

info = f"""
---------------------
{"21*":^21}
---------------------
 Dealer must draw to
 16 and stand on 17.
---------------------
hit  | Throw the dice
hold | No more throws
---------------------"""

end = """
---------------------
 {}: {} 
---------------------
 {}
---------------------"""

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    while True:
        player_score = 0
        bot_score = 0
        hold = False

        cls()
        print(info)
        while player_score <= 21 and not hold:
            state = input(str(player_score) + " > ").lower()
            if state == "hit": player_score += random.randint(1, 11)
            elif state == "hold": 
                hold = True
                print(f"---------------------\n Player {player_score}\n---------------------")
            else: print(f"Unknown command '{state}'")
        if hold:
            while bot_score < 17:
                time.sleep(0.5)
                bot_score += random.randint(1, 11)
                print("*", bot_score)
        if player_score > 21:
            print(end.format("Player", player_score, "Busted! Dealer wins!"))
        elif bot_score > 21:
            print(end.format("Dealer", bot_score, "Dealer busted! Player wins!"))
        elif player_score == bot_score:
            print(end.format("Dealer", bot_score, "Draw!"))
        else:
            print(end.format("Dealer", bot_score, "Dealer win!"))
        input("Press enter to play again")
if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import os

info = """.: PLATESPOTTER :.
------------------
{plate:^17}
------------------"""
def cls():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    startingMessage = "*Searching*"
    last = startingMessage   
    while True:
        cls()
        print(info.format(plate=last))
        new = input("> ")

        if len(new) == 6:
            if last == startingMessage:
                if new[3:6] == "001": last = new.upper()
            elif not any([char.isdigit() for char in new[0:3]]) and new[3:6].isdigit():
                if (int(last[3:6]) + 1) == int(new[3:6]):
                    last = new.upper()
                    if int(last[3:6]) == 999:
                        print("The End")
                        input("Press Enter To exit")
                        exit()
            else:
                input("Invalid Licence Plate\nPress Enter to continue")
        else:
            input("Invalid Licence Plate\nPress Enter to continue")



if __name__ == "__main__": main()

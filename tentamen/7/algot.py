#!/usr/bin/env python3
import os

info = """.: Crazy Shapes :.
------------------
sq | Draw Square
tr | Draw Triangle
------------------
"""

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def getHeight():
    while True:
        height = input("Height = ") 
        print("------------------")
        try:
            height = int(height)
        except NumberError:
            print("Input is not a Number")

        if height > 9:
            print("Height must be smaller than 9")
            continue
        elif height < 1:
            print("height must be larger that 0")
            continue
        return height
        print("------------------")


def main():
    while True:
        cls()

        print(info)

        command = input("shape = ").lower()
        if command == "sq":
            height = getHeight()
            for each in range(height):
                print("#" * height * 2)
        elif command == "tr":
            height = getHeight()
            for each in range(height + 1):
                print(("#"*(each*2-1)).center(height*2-1).center(17))
        else: print("Invalid command '" + command + "'")
        print("------------------")
        input("Press Enter to continue")
            

if __name__ == "__main__": main()

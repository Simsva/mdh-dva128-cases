#!/usr/bin/env python3
import os

info = """
---------------------
       TODOIFY
---------------------
{todos}
---------------------
 add | Add todo
 rm  | Remov todo
---------------------
"""
def cls():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    todos = []
    while True:
        cls()
        print(info.format(todos='\n'.join(["[{}] {}".format(todo[0], todo[1]) for todo in enumerate(todos)])))
        command = input("action > ").lower()
        if command == "add": todos.append(input("todo > "))
        elif command == "rm": 
            while True:
                index = input("index > ")
                try:
                    del todos[int(index)]
                    break 
                except IndexError:
                    print("Index Does not exist '" + index + "'")
                except ValueError:
                    print("Invalid Index '" + index + "'")
        else: 
            print("invalid command '" + command + "'")
            input("Press Enter to continue")


if __name__ == "__main__": main()

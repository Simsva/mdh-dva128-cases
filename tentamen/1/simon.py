#!/usr/bin/env python3

import os, sys

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def add_todo(todos):
    todos.append(input("add > "))
    return todos

def remove_todo(todos):
    try:
        inp = int(input("index > "))
        if inp < len(todos):
            del todos[inp]
            return todos
    except ValueError:
        pass

    sys.stderr.write("Invalid todo id\n")
    return todos

def main():
    oper_help = """\
--------------------------
{title:^25}
--------------------------
{todos}
--------------------------
add | Add todo
rm  | Remove todo
q   | Quit
--------------------------"""

    operations = {
        "add": add_todo,
        "rm": remove_todo,
        # It is really janky to pass todos to sys.exit, but it works
        "q": sys.exit,
    }

    todos = []

    while True:
        cls()
        print(oper_help.format(
            title="TODOIFY",
            todos='\n'.join([ "[{0}] {1}".format(x[0], x[1]) for x in enumerate(todos) ]),
        ))

        oper = input("Selection > ")
        if oper in operations:
            # I want to pass by reference but this isn't C
            todos = operations[oper](todos)
        else:
            sys.stderr.write("ERROR: No such command: '{}'\n".format(oper))

if __name__ == '__main__':
    main()

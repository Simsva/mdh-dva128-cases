#!/usr/bin/env python3
# vim: sw=2 ts=2 et

import os
import json

todos = list()

def cls():
  # This seems really jank but apparently most people do it
  os.system("cls" if os.name == "nt" else "clear")

def list_todos():
  print('-'*40)
  for todo in enumerate(todos):
    print("{index} | [{check}] {desc}".format(index=todo[0], check=('X' if todo[1]["check"] else ' '), desc=todo[1]["desc"]))
  print('-'*40)

def get_index():
  i = -1
  while not 0 <= i < len(todos):
    i_str = input("Todo index > ")
    if i_str.isdigit():
      i = int(i_str)
  return i

def oper_add():
  print('-'*40)
  desc = input("Todo description > ")
  todos.append({"check": False, "desc": desc})
  print('-'*40)
  print("SUCCESS: Todo added")

def oper_check():
  list_todos()
  i = get_index()

  todos[i]["check"] = not todos[i]["check"]
  print('-'*40)
  print("SUCCESS: {}".format("Checked" if todos[i]["check"] else "Unchecked"))

def oper_delete():
  list_todos()
  i = get_index()

  todos.pop(i)
  print('-'*40)
  print("SUCCESS: Todo deleted")

def oper_save():
  try:
    with open("todo.json", 'w') as f:
      f.write(json.dumps(todos))
    print("SUCCESS: Todos saved to file")
  except IOError:
    print("FAILURE: Todos cannot be saved")

def oper_load():
  try:
    with open("todo.json", 'r') as f:
      global todos
      todos = json.loads(f.read())
    print("SUCESS: Todos loaded from file")
  except IOError:
    print("FAILURE: Todos cannot be loaded")
  except json.JSONDecodeError:
    print("FAILURE: 'todo.json' is corrupted")

def main():
  operations = {
    "list":   list_todos,
    "add":    oper_add,
    "check":  oper_check,
    "delete": oper_delete,
    "save":   oper_save,
    "load":   oper_load
  }

  oper_help = """\
****************************************
                Todoify                 
----------------------------------------
list   | List todos
add    | Add todo
check  | Check todo
delete | Delete todo
----------------------------------------
save   | Save todos to file
load   | Load toos from file
----------------------------------------"""
  
  while True:
    cls()
    print(oper_help)

    oper = input("Selection > ")
    if oper in operations:
      operations[oper]()
    else:
      print('-'*40)
      print("ERROR: Unknown command '{}'".format(oper))

    input("Press enter to continue...")

if __name__ == "__main__":
  main()

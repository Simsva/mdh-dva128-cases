#!/usr/bin/env python3
# vim: sw=2 ts=2 et

class todo:
  def __init__(self, action, time, place):
    self.check = " "
    self.action = action
    self.time = time
    self.place = place


help_msg = '''\
==============================
| Operations:                |
|----------------------------|
| <Exit> exit the script     |
| <Help> Prints help message |
| <List> List entire list    |
| <Add> Adds a todo          |
| <Remove> Removes a todo    |
| <Check> Checks a todo      |
| <Uncheck> Unchecks a todo  |
==============================\
'''

todo_list = [todo("action1", "15:00", "place1"),
             todo("action2", "time2", "place2")]
print(help_msg)
while(True):
  query = input("Selection: ").lower()
  if query == "exit":
    break
  elif query == "list":
    print("ToDo:")
    i = 0
    while i < len(todo_list):
      print("Id: ", i, ", [", todo_list[i].check, "]", " ,",
        todo_list[i].action, ", ", todo_list[i].time, " at ", todo_list[i].place)
      i += 1
  elif query == "add":
    todo_list.append(todo(input("What to do?: "),
      input("When?: "), input("Where?: ")))
  elif query == "remove":
    del todo_list[int(input("Enter Id: "))]
  elif query == "check":
    todo_list[int(input("Enter Id: "))].check = "x"
  elif query == "uncheck":
    todo_list[int(input("Enter Id: "))].check = " "
  elif query == "help":
    print(help_msg)
  else:
    print("invalid operation")

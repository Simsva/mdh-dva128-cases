#!/usr/bin/env python3
# vim: sw=2 ts=2 et

import re
from dataclasses import dataclass

# TODO: Dynamically generate usage from list of actions to be similar to Case 1?

## Functions/Classes
@dataclass
class Todo:
  id: int
  action: str
  time: str
  place: str
  check: bool = False

def todo_from_id(id):
  for i in range(len(todo_list)):
    if todo_list[i].id == id:
      return i
  return -1

# Remove ANSI escape sequences from a string
def remove_ansi(string):
  ansi_regex = re.compile(r"\x1b\[[0-9;]*m")
  return ansi_regex.sub("", string)

# Generate a ascii text box around text
def generate_textbox(title, body, minlength=0):
  # Remove ANSI codes for length calculations
  raw_title = remove_ansi(title)
  raw_body = [ remove_ansi(line) for line in body ]

  # Get longest line in box or minlength
  length = max(minlength, len(raw_title), max(len(line) for line in raw_body))

  # Make sure title can be centered
  length += abs(length % 2 - len(raw_title) % 2)
  title_pad = ' '*((length-len(raw_title))//2)

  # Format each body line from raw length
  formatted_body = '\n'.join([ "| {line}{line_pad} |".format(
    line_pad=' '*(length-len(raw_body[i])),
    line=body[i]
  ) for i in range(len(body)) ])

  return '''{eq}
| {title_pad}{title}{title_pad} |
|{dash}|
{body}
{eq}'''.format(eq='='*(length+4), title_pad=title_pad, title=title, dash='-'*(length+2), body=formatted_body, length=length)

## Options
usage_actions = [
  "<\x1b[4mexit\x1b[m> Exit",
  "<\x1b[4mhelp\x1b[m> Print usage",
  "<\x1b[4mlist\x1b[m> List todo entries",
  "<\x1b[4madd\x1b[m> Add new todo",
  "<\x1b[4mremove\x1b[m> Removes a todo",
  "<\x1b[4mcheck\x1b[m> Checks a todo",
  "<\x1b[4muncheck\x1b[m> Unchecks a todo"
]

list_fmt = "ID: {id} - [{check}] {action}, {time} at {place}"

todo_list = [
  Todo(0, "action1", "15:00", "place1"),
  Todo(1, "action2", "time2", "place2")
]

## Code
def main():
  usage = generate_textbox(
    title="\x1b[1mUsage:\x1b[m",
    body=usage_actions
  )
  print(usage)

  while(True):
    query = input("Selection: ").lower()
    if query == "exit":
      break
    elif query == "list":
      print("Todo:")
      for todo in todo_list:
        print(list_fmt.format(
          id=todo.id,
          check="x" if todo.check else " ",
          action=todo.action,
          time=todo.time,
          place=todo.place
        ))
    elif query == "add":
      todo_list.append(Todo(
        len(todo_list),
        input("What to do?: "),
        input("When?: "),
        input("Where?: ")
      ))
    elif query == "remove":
      id = int(input("Enter ID: "))
      i = todo_from_id(id)
      if i < 0:
        print("Invalid ID: '{0}'".format(id))
      else:
        del todo_list[i]
    elif query == "check":
      id = int(input("Enter ID: "))
      i = todo_from_id(id)
      if i < 0:
        print("Invalid ID: '{0}'".format(id))
      else:
        todo_list[i].check = True
    elif query == "uncheck":
      id = int(input("Enter ID: "))
      i = todo_from_id(id)
      if i < 0:
        print("Invalid ID: '{0}'".format(id))
      else:
        todo_list[i].check = False
    elif query == "help":
      print(usage)
    else:
      print("Invalid operation: '{0}'".format(query))

if __name__ == "__main__":
  main()

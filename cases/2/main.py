#!/usr/bin/env python3
# vim: sw=2 ts=2 et

import re
import json
from dataclasses import dataclass

# TODO: Dynamically generate usage from list of actions to be similar to Case 1?

# Functions/Classes


@dataclass
class Todo:
    action: str
    time: str
    place: str
    check: bool = False


# Remove ANSI escape sequences from a string


def remove_ansi(string):
    ansi_regex = re.compile(r"\x1b\[[0-9;]*m")
    return ansi_regex.sub("", string)

# Generate a ascii text box around text


def generate_textbox(title, body, minlength=0):
    # Remove ANSI codes for length calculations
    raw_title = remove_ansi(title)
    raw_body = [remove_ansi(line) for line in body]

    # Get longest line in box or minlength
    length = max(minlength, len(raw_title), max(len(line)
                 for line in raw_body))

    # Make sure title can be centered
    length += abs(length % 2 - len(raw_title) % 2)
    title_pad = ' '*((length-len(raw_title))//2)

    # Format each body line from raw length
    formatted_body = '\n'.join(["| {line}{line_pad} |".format(
        line_pad=' '*(length-len(raw_body[i])),
        line=body[i]
    ) for i in range(len(body))])

    return '''{eq}
| {title_pad}{title}{title_pad} |
|{dash}|
{body}
{eq}'''.format(eq='='*(length+4), title_pad=title_pad, title=title, dash='-'*(length+2), body=formatted_body, length=length)


# Options
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
]

with open('todos.txt', 'r') as read_file:
    temp_array = json.loads(read_file.read())
    for todo in temp_array:
        todo_list.append(Todo(*todo.values()))


# Code


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
            for idx, todo in enumerate(todo_list):
                print(list_fmt.format(
                    id=idx,
                    check="x" if todo.check else " ",
                    action=todo.action,
                    time=todo.time,
                    place=todo.place
                ))
        elif query == "add":
            todo_list.append(Todo(
                input("What to do?: "),
                input("When?: "),
                input("Where?: ")
            ))
        elif query == "remove":
            id = int(input("Enter ID: "))
            if id < 0:
                print("Invalid ID: '{0}'".format(id))
            else:
                del todo_list[id]
        elif query == "check":
            id_str = input("Enter ID: ")
            try:
                id = int(id_str)
                if id < 0:
                    print("Invalid ID: '{0}'".format(id))
                else:
                    todo_list[id].check = True
            except ValueError:
                print("Invalid input: '" + id_str + "'")
        elif query == "uncheck":
            id_str = input("Enter ID: ")
            if(id_str):
                id = int(input("Enter ID: "))
                if id < 0:
                    print("Invalid ID: '{0}'".format(id))
                else:
                    todo_list[id].check = False
        elif query == "help":
            print(usage)
        else:
            print("Invalid operation: '{0}'".format(query))

        json_string = json.dumps([ob.__dict__ for ob in todo_list])
        with open('todos.txt', 'w') as write_file:
            write_file.write(json_string)
        input("Press ENTER to continue...")


if __name__ == "__main__":
    main()

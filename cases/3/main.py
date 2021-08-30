#!/usr/bin/env python3

import requests
import json
import os

base_url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/" # url to artist list

screens = {
  "main": """
----------------------------------------
            Artists Database
----------------------------------------
| L | Lists artists
| V | View artist profile
| E | Exit application
----------------------------------------
""",
  "artists":  """
----------------------------------------
            Artists Database
----------------------------------------
{artists}
****************************************
| L | Lists artists
| V | View artist profile
| E | Exit application
----------------------------------------
""",

  "info": """
**************************************** 
{name:^40}
****************************************
| Members:      {members}
| Genres:       {genres}
| Years active: {years_active}
----------------------------------------
| L | Lists artists
| V | View artist profile
| E | Exit application
----------------------------------------
""",

  "unknown": """
----------------------------------------
|
| ERROR: Unknown command '{input}'
|
----------------------------------------
Press enter to continue
""",

  "exit": "SUCCESS: Script exited successfully!",
  "group_error": """
------------------------------------------
|
| ERROR: Artist not found '{input}'
|
------------------------------------------
Press enter to continue
  """,
  "group_input": """
----------------------------------------
            Artists Database
----------------------------------------
Input Name:
  """
}

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def get_data(url):
  return_string = requests.get(url) # gets json string of data
  return_object = json.loads(return_string.text) # converts json string to dict object
  return return_object

def list_artists():
  cls()

  artists = get_data(base_url + "artists/")["artists"]
  artist_list = ""
  for each in artists:
    artist_list = artist_list + "| " + each["name"] + "\n"

  print(screens["artists"].format(artists=artist_list))
  get_action()

def list_group():
  cls()
  print(screens["group_input"])
  artists = get_data(base_url + "artists/")["artists"]
  target_group = input()
  cls()

  id = ""
  for each in artists:
    if each["name"].lower() == target_group.lower():
      id = each["id"]

  if id:
    data = get_data(base_url + "artists/" + id + "/")["artist"]

    genres = ", ".join(data["genres"])
    name = data["name"]
    years_active = ", ".join(data["years_active"])
    members = ", ".join(data["members"])

    print(screens["info"].format(genres=genres, name=name, years_active=years_active, members=members))
    get_action()

  else:
    print(screens["group_error"].format(input=target_group))
    input()
    cls()
    print(screens["main"])
    get_action()


def get_action():
  action = input().lower().strip()

  if action == "l":
    list_artists()

  elif action == "v":
    list_group()

  elif action == "e":
    print(screens["exit"])
    exit()

  else:
    cls()
    print(screens["unknown"].format(input=action))
    input()
    cls()
    print(screens["main"])
    get_action()

cls()
print(screens["main"])
get_action()

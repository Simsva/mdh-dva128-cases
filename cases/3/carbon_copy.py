#!/usr/bin/env python3

import requests
import os, sys

api_url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/"

def cls():
    os.system("cls" if os.name=="nt" else "clear")

def get_data(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    else:
        sys.stderr.write("ERROR: Failed to get data from API\n")

def list_artists():
    cls()

    artists = get_data("{}artists/".format(api_url))["artists"]
    artist_list = '\n'.join(map(lambda a: "| {}".format(a["name"]), artists))

    print("""\
----------------------------------------
            Artists Database
----------------------------------------""")
    print(artist_list)
    print('-'*40)

    # Return artists for use in view_artists
    return artists

def view_artist():
    print("Doin' your mom")
    artists_raw = list_artists()
    # i: { "name", "id" } => { "name": "id" }
    artists = dict(map(lambda a: (a["name"].lower(), a["id"]), artists_raw))

    artist_name = input("Selection > ")
    if artist_name in artists:
        data = get_data("{0}artists/{1}/".format(api_url, artists[artist_name]))["artist"]

        info = dict()
        info["name"] = data["name"]
        info["genres"] = ", ".join(data["genres"])
        info["years_active"] = ", ".join(data["years_active"])
        info["members"] = ", ".join(data["members"])

        info_text = """\
----------------------------------------
{name:^40}
----------------------------------------
| Members:      {members}
| Genres:       {genres}
| Years active: {years_active}
----------------------------------------"""
        # Deconstruct dict to function arguments
        print(info_text.format(**info))
    else:
        sys.stderr.write("ERROR: Unknown artist: '{}'\n".format(artist_name))

def main():
    operations = {
        "l": list_artists,
        "v": view_artist,
        "q": sys.exit,
    }

    oper_help = """\
----------------------------------------
            Artists Database
----------------------------------------
| L | Lists artists
| V | View artist profile
| Q | Quit application
----------------------------------------"""

    while True:
        cls()
        print(oper_help)

        oper = input("Selection > ").lower()
        if oper in operations:
            operations[oper]()
        else:
            print('-'*40)
            sys.stderr.write("ERROR: Unknown command '{}'\n".format(oper))

        input("Press enter to continue...")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import os, sys
import requests

version = "1.0.1"

api = "http://football-frenzy.s3-website.eu-north-1.amazonaws.com/api"

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def get_json(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    elif r.status_code == 404:
        sys.stderr.write("ERROR: Season ")
    else:
        sys.stderr.write("ERROR: Failed to get data from API\n")

    sys.exit(1)

def list_seasons():
    data = None
    r = requests.get(api)
    if r.status_code == 200:
        data = r.json()["seasons"]
    else:
        sys.stderr.write("ERROR: Failed to get seasons from API\n")
        return

    print('-'*40)
    print('\n'.join(map(lambda x: f"| {x}", data)))
    print('-'*40)

def view_season():
    year = input("Year > ")

    data = None
    r = requests.get(f"{api}/{year}")
    if r.status_code == 200:
        data = r.json()
    else:
        sys.stderr.write(f"ERROR: Season '{year}' not found\n")
        return

    # Overall game statistics
    #   index: [team_name, wins, draws, losses, points]
    stats = list(map(lambda x: [x[1], 0, 0, 0, 0], enumerate(data["teams"])))
    # Map team name to index
    team_to_index = dict(map(lambda x: (x[1][0], x[0]), enumerate(stats)))

    # Loop through all game days
    for day in data["gamedays"]:
        r = requests.get(f"{api}/{year}/{day}")
        if r.status_code != 200:
            sys.stderr.write("ERROR: Failed to get gameday info\n")
            sys.exit(1)
        else:
            # Loop through all games
            for game in r.json()["games"]:
                home = game["score"]["home"]
                away = game["score"]["away"]
                home_index = team_to_index[home["team"]]
                away_index = team_to_index[away["team"]]

                if home["goals"] > away["goals"]:
                    # Add win and points to home, and loss to away
                    stats[home_index][1] += 1
                    stats[home_index][4] += 3

                    stats[away_index][3] += 1
                elif home["goals"] < away["goals"]:
                    # Add win and points to a away, and loss to home
                    stats[away_index][1] += 1
                    stats[away_index][4] += 3

                    stats[home_index][3] += 1
                else:
                    # Add draw and points to both
                    stats[home_index][2] += 1
                    stats[home_index][4] += 1

                    stats[away_index][2] += 1
                    stats[away_index][4] += 1

    # Maximum length of every column, used for formatting
    #   index_in_stats: length
    max_length = list(map(
        # Calculate maximum of every value in column
        lambda x: max([ len(str(row[x])) for row in stats ]),
        range(len(stats[0]))
    ))

    # Set minimum length to 3
    for i in range(len(max_length)):
        if max_length[i] < 3:
            max_length[i] = 3

    total_length = sum(max_length) + 10

    print('*'*total_length)
    print("| {team:<{team_len}}  {wins:>{wins_len}}  {draws:>{draws_len}}  {losses:>{losses_len}}  {points:>{points_len}}".format(
        team="Team", team_len=max_length[0],
        wins="W", wins_len=max_length[1],
        draws="D", draws_len=max_length[2],
        losses="L", losses_len=max_length[3],
        points="P", points_len=max_length[4],
    ))
    print('-'*total_length)
    print('\n'.join(map(
        lambda x: f"| {x[0]:<{max_length[0]}}  {x[1]:>{max_length[1]}}  {x[2]:>{max_length[2]}}  {x[3]:>{max_length[3]}}  {x[4]:>{max_length[4]}}",
        stats
    )))
    print('*'*total_length)

def main():
    operations = {
        "list": list_seasons,
        "view": view_season,
        "quit": sys.exit
    }

    oper_help = """\
****************************************
            FOOTBALL FRENZY
              STAT VIEWER
{version:^40}
----------------------------------------
| list | List available seasons
| view | View table for season
| quit | Quit the program
----------------------------------------""".format(version=version)

    while True:
        cls()
        print(oper_help)

        oper = input("Selection > ").lower()
        if oper in operations:
            operations[oper]()
        else:
            print('-'*40)
            sys.stderr.write("ERROR: Unknown command '{}'\n".format(oper))

        input("Press ENTER to continue...")

if __name__ == '__main__':
    main();

#!/usr/bin/env python3

import os
from data import db

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    menu = """\
--------------------------
{title:^25}
--------------------------""".format(title="Age Stat Viewer")

    while True:
        cls()
        print(menu)
        occupation = input("Occupation > ")

        stats = {
            # Assume age ranges from 0 to 99, i.e. ten spans of ten years
            "age": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            "female": 0,
            "male": 0,
        }
        for person in filter(lambda x: x["occupation"] == occupation, db):
            if person["female"]:
                stats["female"] += 1
            else:
                stats["male"] += 1

            age_range = person["age"] // 10
            stats["age"][age_range] += 1

        print('-'*25)
        print('\n'.join(
            "| {label:<5} | {value}".format(
                # Label based on age index
                label=f"{x[0]*10}-{(x[0]+1)*10 - 1}",
                value=x[1]
            ) for x in enumerate(stats["age"]) if x[1] != 0
        ))
        print('-'*25)
        print(f"| FEMALE | {stats['female']}\n| MALE   | {stats['male']}")
        print('-'*25)

        input("Press ENTER to search again...")

if __name__ == '__main__':
    main()

#!/usr/bin/env python3

result = {
  "Belgien": {
    "GP": 3,
    "W": 1,
    "L": 0,
    "D": 2,
    "GD": 3,
    "P": 5
  },
  "Frankrike": {
    "GP": 3,
    "W": 1,
    "L": 1,
    "D": 1,
    "GD": 2,
    "P": 4
  },
  "Brasilien": {
    "GP": 3,
    "W": 0,
    "L": 1,
    "D": 2,
    "GD": -4,
    "P": 2
  },
  "England": {
    "GP": 3,
    "W": 1,
    "L": 1,
    "D": 1,
    "GD": -1,
    "P": 4
  }
}
def main():
    print('-'*45)
    print("| # | Team       | GP | W | L | D | GD  | P |")
    print('-'*45)
    i = 0
    for k, v in sorted(result.items(), key=lambda x: (x[1]["P"], x[1]["GD"]), reverse=True):
        print("| {0:>1} | {1:<10} | {GP:>2} | {W:>1} | {L:>1} | {D:>1} | {GD:>3} | {P:>1} |".format(
            i := i+1,
            k,
            **v,
        ))
    print('-'*45)

    # One liner for true chads
#     print("""\
# ---------------------------------------------
# | # | Team       | GP | W | L | D | GD  | P |
# ---------------------------------------------
# {values}
# ---------------------------------------------""".format(values='\n'.join(
#         [ "| {0:>1} | {1:<10} | {GP:>2} | {W:>1} | {L:>1} | {D:>1} | {GD:>3} | {P:>1} |".format(x[0], x[1][0], **x[1][1]) for x in enumerate(sorted(result.items(), key=lambda x: (x[1]["P"], x[1]["GD"]), reverse=True)) ]
#     )))

if __name__ == '__main__':
    main()

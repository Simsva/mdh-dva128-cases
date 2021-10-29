#!/usr/bin/env python3

import os, sys

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def error(msg):
    sys.stderr.write("ERROR: " + msg)
    input("Press ENTER to continue...")

def get_account(accounts, prompt):
    account = input(prompt)
    if account in accounts:
        return account
    else:
        error(f"No such account: {account}\n")
        return

def open_account(accounts):
    while True:
        name = input("Account name > ")
        if name in accounts:
            error("Account already exists\n")
        else:
            accounts[name] = 0
            return accounts

def close_account(accounts):
    name = get_account(accounts, "Account name > ")
    if name == "main":
        error("Cannot delete a protected account\n")
    else:
        if accounts[name] != 0:
            error("Account is not empty\n")
        else:
            del accounts[name]

    return accounts

def transfer_money(accounts):
    sender = get_account(accounts, "Sender > ")
    if not sender: return accounts
    receiver = get_account(accounts, "Receiver > ")
    if not receiver: return accounts

    if sender == receiver:
        error("Cannot transfer money from and to the same account\n")
    else:
        while True:
            try:
                amount = int(input("Amount > "))
                if amount < 0:
                    # Inputting zero is the only way to escape if sender has no money
                    error("Cannot send amounts less than zero\n")
                elif amount > accounts[sender]:
                    error("Insufficient funds\n")
                else:
                    accounts[sender] -= amount
                    accounts[receiver] += amount
                    break
            except ValueError:
                error("Invalid amount\n")

    return accounts

def main():
    accounts = {
        "main": 1000,
    }

    oper_help = """\
--------------------------
{title:^25}
--------------------------
{accounts}
--------------------------
o | Open an account
c | Close an account
t | Transfer money
q | Quit
--------------------------"""

    operations = {
        "o": open_account,
        "c": close_account,
        "t": transfer_money,
    }

    while True:
        cls()
        print(oper_help.format(
            title="Account Manager",
            accounts='\n'.join([ "| {}: {}".format(*x) for x in accounts.items() ])
        ))

        oper = input("Selection > ").lower()
        if oper == "q":
            sys.exit()
        elif oper in operations:
            accounts = operations[oper](accounts)
        else:
            error(f"No such command: '{oper}'\n")

if __name__ == '__main__':
    main()

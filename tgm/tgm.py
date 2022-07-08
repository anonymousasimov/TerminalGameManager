#!/usr/bin/python
from copyreg import dispatch_table
import os
import json
from random import gammavariate

from rich.console import Console
from rich.table import Table
from rich import box

from pyfiglet import figlet_format as pyfig

console = Console()

def getGames() -> dict:
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    with open(os.path.join(__location__, "terminalGames.json"), "r") as tg:
        terminalGames = json.load(tg)
    return terminalGames
    
def send_command(i):
    if int(i) + 1 > len(getGames()):
        print("selected game is invalid")
    else:
        selectedGame = getGames()[int(i)]
        os.system(selectedGame["command"])

def display_menu():
    titleTable = Table (
        style = "#E1AD01",
        box=box.SIMPLE_HEAVY, 
    )

    titleTable.add_column(pyfig("Terminal Games"), style="#E1AD01")
    titleTable.add_column("id", style="#E1AD01")

    i = 0
    for game in getGames():
        titleTable.add_row(game["title"],str(i))
        i += 1

    console.print(titleTable)

def main():
    listening = True
    while listening:
        cmd = input()
        cmd = cmd.split()
        if len(cmd) > 0:
            if cmd[0] == "help":
                print("There is no help atm")
            elif cmd [0] == "quit":
                listening = False
            elif cmd [0] == "display":
                display_menu()
            elif cmd [0] == "run":
                if len(cmd) == 2:
                    send_command(cmd[1])
                else:
                    print("Error: unkown command. Try\nhelp")

            else:
                print("Error: unkown command. Try\nhelp")
        else:
           print("Error: unkown command. Try\nhelp")


display_menu()
main()
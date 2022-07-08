#!/usr/bin/python
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

display_menu()
import os
import json
import typer

from rich.console import Console
from rich.table import Table
from rich import box

from pyfiglet import figlet_format as pyfig

console = Console()
app = typer.Typer()

def getGames() -> dict:
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    with open(os.path.join(__location__, "terminalGames.json"), "r") as tg:
        terminalGames = json.load(tg)
    return terminalGames

@app.command(short_help="Runs the selected terminal game") 
def start(game_id: int) -> None:
    gameList = getGames()
    if game_id + 1 > len(gameList):
        print("selected game is invalid")
    else:
        selectedGame = gameList[game_id]
        os.system(selectedGame["command"])

@app.command(short_help="Display list of terminal games")
def display():
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

if __name__ == "__main__":
    app()

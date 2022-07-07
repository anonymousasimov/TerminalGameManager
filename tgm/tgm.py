from rich.console import Console
from rich.table import Table
from rich import box

from pyfiglet import figlet_format as pyfig

console = Console()

def display_menu():
    titleTable = Table (
        style = "#E1AD01",
        box=box.SIMPLE_HEAVY, 
    )

    titleTable.add_column(pyfig("Terminal Games"), style="#E1AD01")

    console.print(titleTable)

display_menu()
#!/usr/bin/python

from rich.console import Console
from rich.table import Table
from rich import box

from pyfiglet import figlet_format as pyfig

console = Console()

titleTable = Table (
    style = "#E1AD01",
    box=box.SIMPLE_HEAVY, 
)

titleTable.add_column(pyfig("Terminal Games"), style="#E1AD01")
#table_print(titleTable)
console.print(titleTable)
# TerminalGameManager
Terminal based interface to keep games that run in the terminal orgranised in one place.

# Installation Guide
This program requires the following python modules to function:<br>
- rich
- typer
- pyfiglet
<br>
To install these use:

```bash
  pip install [package name]

  #if pip doesnt work instead use pip3
```

For example:

```bash
  pip install rich
```
Once all the required packages are installed type the following commands:

```bash
  cd ~
  git clone "https://github.com/anonymousasimov/TerminalGameManager.git"
```
Then open your ~/.bashrc file in an editor of your choice and add<br>
the following command to it:

```bash
  alias tgm='~/TerminalGameManager/tgm/tgm'
```

Then restart your terminal. You can now run the cli using the command 'tgm'.
Run tgm --help for help.

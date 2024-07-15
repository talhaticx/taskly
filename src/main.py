from todos import app
from _utils import *
from rich.layout import Layout
from rich.panel import Panel
from rich import print

def main():
    clear_terminal()
    cool_text("Todos")
    while True:
        done = app()
        if done == 0:
            break


if __name__ == "__main__":
    clear_terminal()
    cool_text("Todos")

    main()
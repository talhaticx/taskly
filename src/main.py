from rich import print
from rich.layout import Layout
from rich.panel import Panel

from _utils import *
from todos import app


def main():
    """main function"""

    clear_terminal()
    cool_text("Todos")
    while True:
        done = app()
        if done == 0:
            break


if __name__ == "__main__":
    main()

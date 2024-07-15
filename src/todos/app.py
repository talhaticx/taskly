import os
from typing import List, Tuple

from _utils import *

from ._todo import todo
from .maindb import *

DatabaseType = List[Tuple[int, str, str]]

@caution()
def app():
    settings = Settings.get_data()['settings']

    db_file = os.path.expanduser(f"~/todos/{settings["main_db"]}.db")

    # Ensure the directory exists
    db_dir = os.path.dirname(db_file)
    os.makedirs(db_dir, exist_ok=True)
    
    cursor, conn = db_connect(db_file)
    databases:  DatabaseType = db_query(cursor)
    
    if len(databases) != 0:    
        printList(databases)
        console.print("Enter 'n' for new database\nEnter 'd' for deleting a database\nEnter id for opening a database\nEnter Choice: ", style="bold italic Blue", end="")
        choice = input()
    else:
        choice = 'n'

    if choice == 'n':
        db_add(cursor, conn)
    elif choice == 'd':
        db_delete(cursor, conn, databases)

    # ! don't remove this, necessary for exiting the program and also for the correct functionality of the program
    elif choice == '0':
        console.print("Exiting...", style="red bold")
        cursor.close()
        conn.close()
        return 0
    else:
        cursor.close()
        conn.close()
        # // print(databases)
        try:
            # ! When 0 is entered the the index become -1 which refers to the last item in the database list.
            todo(databases[int(choice)-1][1])
        except IndexError:
            console.print("Invalid ID", style="red bold")


if __name__ == "__main__":
    app()
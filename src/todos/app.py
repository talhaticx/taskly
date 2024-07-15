from ._todo import todo
from _utils import *
import os
import sqlite3

def db_connect(file):
    conn = sqlite3.connect(file)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks_list (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            description TEXT
        )
    ''')
    
    return cursor, conn

@cation()
def db_query(cursor):
    cursor.execute("Select * FROM tasks_list")
    data = cursor.fetchall()
    return data

@cation()
def db_add(cursor, conn):
    console.print("\nAdding a new Database\n", style="bold green", justify="center" )
    name = console.input(("[b][i]Enter Name: [/i][/b] "))
    while name == "":
        name = console.input(("[b][i]Enter Name: [/i][/b] "))
    description = console.input(("[b][i]Enter Description: [/i][/b] "))
    try:
        cursor.execute('''
            INSERT INTO tasks_list (name, description)
            VALUES (?, ?)
        ''', (name, description))
        console.print("Database was added", style="green bold")
        conn.commit()
    except sqlite3.IntegrityError:
        print("Task with the same Name already exists.")
        
@cation()
def db_delete(cursor, conn, tasks):
    printList(tasks)
    id = console.input("[b][i]Enter ID: [/i][/b] ")
    
    cursor.execute('''
        DELETE FROM tasks_list
        WHERE id = ?               
    ''', (id,))
    conn.commit()
    try:
        delete_file(f'{Settings.get_data()["database_dir"]}{tasks[id]}.db')
    except:
        print("Fuck You")


@cation()
def app():
    settings = Settings.get_data()['settings']

    db_file = os.path.expanduser(f"~/todos/{settings["main_db"]}.db")

    # Ensure the directory exists
    db_dir = os.path.dirname(db_file)
    os.makedirs(db_dir, exist_ok=True)
    
    cursor, conn = db_connect(db_file)
    databases = db_query(cursor)
    
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
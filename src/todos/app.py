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
    
def db_query(cursor):
    cursor.execute("Select * FROM tasks_list")
    data = cursor.fetchall()
    return data
    
def db_add(cursor, conn):
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
        
        
def db_delete(cursor, conn, tasks):
    printList(tasks)
    id = console.input(("[b][i]Enter ID: [/i][/b] "))
    
    cursor.execute('''
        DELETE FROM tasks_list
        WHERE id = ?               
    ''', (id,))
    conn.commit()

def app():
    settings = Settings.get_data()['settings']

    db_file = os.path.expanduser(f"~/todos/{settings["main_db"]}.db")

    # Ensure the directory exists
    db_dir = os.path.dirname(db_file)
    os.makedirs(db_dir, exist_ok=True)
    
    cursor, conn = db_connect(db_file)
    databases = db_query(cursor)
    
    console.print(databases)
    
    if len(databases) != 0:    
        clear_terminal()
        printList(databases)
        console.print("\n\nEnter 'n' for new database\nEnter 'd' for deleting a database\nEnter id for opening a database\nEnter Choice: ", style="bold italic Blue", end="")
        choice = input()
    else:
        clear_terminal()
        choice = 'n'

    if choice == 'n':
        db_add(cursor, conn)
    elif choice == 'd':
        db_delete(cursor, conn, databases)
    elif choice == '0':
        console.print("Exiting...", style="red bold")
        cursor.close()
        conn.close()
        exit()
    else:
        cursor.close()
        conn.close()
        try:
            todo(databases[int(choice)-1][1])
        except IndexError:
            console.print("Invalid ID", style="red bold")
    
        
    



if __name__ == "__main__":
    app()
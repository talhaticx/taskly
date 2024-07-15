import sqlite3
from _utils import *

@caution()
def db_connect(file:str):
    """connects to the main database where list of task databases is stored

    Args:
        file (str): name of the database to connect to

    Returns:
        sqlite3 objects: cursor object and connector object
    """
    
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

@caution()
def db_query(cursor):
    """queries main database

    Args:
        cursor (sqlite3 object): cursor

    Returns:
        list of tuple ('id', 'name', 'description')
    """
    
    cursor.execute("Select * FROM tasks_list")
    data = cursor.fetchall()
    return data

@caution()
def db_add(cursor, conn):
    """add data to the database

    Args:
        cursor (sqlite3 object): cursor
        conn (sqlite3 object): connection
    """
    
    console.print("\nAdding a new Database\n", style="bold green", justify="center" )
    name = console.input(("[b][i]Enter Name: [/i][/b] "))
    while name == "":
        name = console.input(("[b][i]Enter Name: [/i][/b] "))
    description = console.input(("[b][i]Enter Description: [/i][/b]"))
    try:
        cursor.execute('''
            INSERT INTO tasks_list (name, description)
            VALUES (?, ?)
        ''', (name, description))
        console.print("Database was added", style="green bold")
        conn.commit()
    except sqlite3.IntegrityError:
        print("Task with the same Name already exists.")
        
@caution()
def db_delete(cursor, conn, tasks):
    """deletes data from the database

    Args:
        cursor (sqlite3 object): cursor
        conn (sqlite3 object): connection
    """
    
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
        print("Error")
        
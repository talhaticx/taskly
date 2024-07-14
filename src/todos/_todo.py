from .databaseClass import Database
from .taskClass import Task
from _utils import *

def todo(name):
    db = Database(name)
    while True:
        todos = db.query()
        
        clear_terminal()
        print()
        printMenu()
        print()
        choice = console.input(("[b][i]Enter your choice:[/i][/b] "))
        
        if choice == "1":
            clear_terminal()
            printTask(db)
            wait_for_enter()
            
        elif choice == "2":
            task = Task()
            db.add_task(task)
            
        elif choice == "3":
            printList(todos)
            id = console.input("[b][i]Enter id to remove:[/i][/b] ")
            db.remove_task(id)
            
        elif choice == "4":
            printList(todos)
            id = console.input("[b][i]Enter id to update description:[/i][/b] ")
            description = console.input("[b][i]Enter new description:[/i][/b] ")
            db.update_description(id, description)
            
        elif choice == "5":
            printList(todos)
            id = console.input("[b][i]Enter id to mark as completed:[/i][/b] ")
            db.update_completed(id, completed=True)
            
        elif choice == "6":
            printList(todos)
            ids = console.input("[b][i]Enter id to mass remove:[/i][/b] ")
            for id in ids:
                db.remove_task(id)
        
        elif choice == "7":
            printList(todos)
            ids = console.input("[b][i]Enter id to mass update:[/i][/b] ")
            for id in ids:
                db.update_completed(id)
            
        elif choice == "0":
            db.exit()
            break
        
        else:
            pass
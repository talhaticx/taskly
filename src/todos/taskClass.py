from _utils import console

class Task(object):
    def __init__(self):
        self.title = str(console.input("[b][i]Enter title:[/b][/i] "))
        while self.title == "":
            self.title = str(console.input("[b][i]Enter title:[/b][/i] "))
        self.description = str(console.input("[b][i]Enter description:[/b][/i] "))
        print()
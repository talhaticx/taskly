import os
import platform

def wait_for_enter():
    input("Press Enter to continue...")
    
def clear_terminal():
    current_os = platform.system()
    if current_os == 'Windows':
        os.system('cls')
        print()
    else:  # Linux and MacOS
        os.system('clear')
        print()
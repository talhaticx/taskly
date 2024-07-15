import sys
import select

def escape():
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        key = sys.stdin.read(1)
        if key == '\x1b':  # '\x1b' is Esc key
            return True
    return False
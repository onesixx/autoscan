import sys
import termios
import tty
import time

print("Press ESC to stop")

while True:
    if sys.stdin in elect.select([sys.stdin], [], [], 0)[0]:
        key = sys.stdin.read(1)  # Get the key that was pressed
        if key == '\x1b':  # ESC key
            print("ESC pressed, stopping...")
            break
    print("Running...")
    time.sleep(1)
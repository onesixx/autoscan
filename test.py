import keyboard
import time

pause = False

def on_key_press(e):
    global pause
    pause = not pause

keyboard.on_press_key('esc', on_key_press)

for i in range(71, 282):
    print(f'ese1: {pause}')
    while True:
        if pause:
            print("----pause")
            time.sleep(1)
            continue
        else:
            print(f'Logic:{i}')
            time.sleep(3)
            break
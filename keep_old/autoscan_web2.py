# pip install pyautogui
# pip install keyboard  
# pip install keyboard  

import pyautogui 
import pyperclip
import keyboard
import time

start_page = 1
total_page = 250
book_name = 'REsilience'
top_x = 1700
top_y = -900
end_x = 2730
end_y =  350
roi = (1700, -900,  abs(end_x-top_x), abs(end_y-top_y))
ebook_screen_next_page =(2736,-242)
sleep_time = 1.0

pause = False
def on_key_press(e):
    global pause
    pause = not pause
keyboard.on_press_key('esc', on_key_press)

time.sleep(3)
print("---start---")
for i in range(int(start_page), int(total_page)):
    while True:
        if pause:
            continue
        else:        
            # ---  make  the name
            file_name = book_name + '_' + str(i).zfill(4) + '.png'

            # ---  Capture 
            screenshot = pyautogui.screenshot(region=roi)
            time.sleep(sleep_time)

            # ---  Save capture
            screenshot.save('./data/{file_name}')
            time.sleep(sleep_time)

            if i%25 == 0 :
                print("==========Check Time=========")
                time.sleep(10)

            # ---  Next Page 
            pyautogui.doubleClick(ebook_screen_next_page)
            # time.sleep(sleep_time)

            # ---  Print result
            print(str(i), '/', int(total_page))
            break

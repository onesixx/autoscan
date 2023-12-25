# pip install pyautogui
# pip install keyboard  
# pip install keyboard  

import pyautogui 
import pyperclip
import keyboard
import time

total_page = 250
book_name = 'wealthinking_2'
mac_outside_widget = (1580,660)
win_outside = (2000, 666)
ebook_screen_next_page =(2736,-282)
sleep_time = 2.0

# --- TEST
# pyautogui.click(ebook_screen_next_page)
# ---  마우스 좌표 구하기
# for i in range(10):
#     time.sleep(3)
#     print(f"{i}th : {pyautogui.position()}")
# ---  화면 size
# print(pyautogui.size ())

time.sleep(3)
print("---start---")
# for i in range(int(total_page)):
for i in range(47, int(total_page)):
    # ---  make  the name
    file_name = book_name + '_' + str(i+1).zfill(4) + '.png'
    pyperclip.copy(file_name)
    time.sleep(sleep_time)

    # ---  Capture 
    pyautogui.click(mac_outside_widget) 
    time.sleep(sleep_time)
    pyautogui.hotkey('shift', 'option','p')
    time.sleep(sleep_time)

    # ---  Save capture
    pyautogui.hotkey('command', 's')
    time.sleep(sleep_time)
    pyautogui.hotkey('command', 'v')
    time.sleep(sleep_time)
    pyautogui.press('enter')
    time.sleep(sleep_time)

    if i%30 == 0 :
        time.sleep(30)

    # ---  Next Page
    # pyautogui.click(win_outside)
    pyautogui.click(ebook_screen_next_page) 
    time.sleep(sleep_time) 
    pyautogui.doubleClick(ebook_screen_next_page)
    #pyautogui.click(ebook_screen_next_page)
    time.sleep(sleep_time)

    # pyautogui.press('right')
    # time.sleep(sleep_time)

    # ---  Print result
    print(str(i), '/', int(total_page))

    # ---  Stop processing : Check if the ESC key is pressed
    if keyboard.is_pressed('esc'):
        break

# pip install pyautogui
# pip install keyboard  

import pyautogui 
import time
import pyperclip
import keyboard

    
# 화면 
# print(pyautogui.size ())

# 마우스 좌표 구하# pip install pyautogui
# pip install keyboard  

import pyautogui 
import time
import pyperclip
import keyboard

    
# 화면 
# print(pyautogui.size ())

# 마우스 좌표 구하기
# for i in range(10):
#     time.sleep(6)
#     print(f"{i}th : {pyautogui.position()}")

total_page = 200
book_name = 'ebook_1'
#capture_pos = (269, 536)
# ebook_screen_center_pos = (935, 595)
ebook_screen_next_page =(930,600)
sleep_time = 1.0

time.sleep(5.)

for i in range(int(total_page)):
    file_name = book_name + '_' + str(i+1).zfill(4) + '.png'
    pyperclip.copy(file_name)
    
    pyautogui.hotkey('shift', 'option','p')
    #pyautogui.click(capture_pos)
    time.sleep(sleep_time)

    pyautogui.hotkey('command', 's')
    time.sleep(sleep_time)

    pyautogui.hotkey('command', 'v')
    time.sleep(sleep_time)
    pyautogui.press('enter')
    time.sleep(sleep_time)

    # pyautogui.click(ebook_screen_next_page)
    pyautogui.doubleClick(ebook_screen_next_page)
    # #pyautogui.click(ebook_screen_center_pos)
    time.sleep(sleep_time)

    # pyautogui.press('right')
    # time.sleep(sleep_time)

    print(str(i+1), '/', int(total_page/2))

    # Check if the ESC key is pressed
    if keyboard.is_pressed('esc'):
        break기
# for i in range(10):
#     time.sleep(6)
#     print(f"{i}th : {pyautogui.position()}")

total_page = 200
book_name = 'ebook_1'
#capture_pos = (269, 536)
# ebook_screen_center_pos = (935, 595)
ebook_screen_next_page =(930,600)
sleep_time = 1.0

time.sleep(5.)

for i in range(int(total_page)):
    file_name = book_name + '_' + str(i+1).zfill(4) + '.png'
    pyperclip.copy(file_name)
    
    pyautogui.hotkey('shift', 'option','p')
    #pyautogui.click(capture_pos)
    time.sleep(sleep_time)

    pyautogui.hotkey('command', 's')
    time.sleep(sleep_time)

    pyautogui.hotkey('command', 'v')
    time.sleep(sleep_time)
    pyautogui.press('enter')
    time.sleep(sleep_time)

    # pyautogui.click(ebook_screen_next_page)
    pyautogui.doubleClick(ebook_screen_next_page)
    # #pyautogui.click(ebook_screen_center_pos)
    time.sleep(sleep_time)

    # pyautogui.press('right')
    # time.sleep(sleep_time)

    print(str(i+1), '/', int(total_page/2))

    # Check if the ESC key is pressed
    if keyboard.is_pressed('esc'):
        break
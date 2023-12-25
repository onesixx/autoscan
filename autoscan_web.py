# pip install pyautogui
# pip install keyboard  
# pip install keyboard  

import pyautogui 
import pyperclip
import time
import keyboard
import os

start_page = 1
total_page = 350
book_name = 'Resilience'
top_x = 1700
top_y = -900
end_x = 2730
end_y =  350
roi = (1700, -900,  abs(end_x-top_x), abs(end_y-top_y))
ebook_screen_next_page =(2735,-275)
sleep_time = 1.0

if not os.path.exists(os.path.join("data", book_name)):
    os.makedirs(os.path.join("data", book_name))

time.sleep(3)
print("---start---")
for i in range(int(start_page), int(total_page)):   
    # ---  make  the name
    file_name = book_name + '_' + str(i).zfill(4) + '.png'

    # ---  Capture 
    screenshot = pyautogui.screenshot(region=roi)
    time.sleep(sleep_time)

    # ---  Save capture
    screenshot.save(f'./data/{book_name}/{file_name}')
    time.sleep(sleep_time)

    if i%25 == 0 :
        print("==========Check Time=========")
        time.sleep(10)

    # ---  Next Page 
    cursor_position = pyautogui.position()    
    if top_x+100 <= cursor_position.x <= end_x+100 and top_y <= cursor_position.y <= end_y:
        pyautogui.click(ebook_screen_next_page)
    else:
        pyautogui.doubleClick(ebook_screen_next_page)
    time.sleep(sleep_time)

    # ---  Print result
    print(str(i), '/', int(total_page))
# 한 Page, 폰트 11
# Pdf 저장
# Pdf 내보내기
# Pdf 용량줄이기
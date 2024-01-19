# pip install pyautogui keyboard  keyboard  
import pyautogui, pyperclip 
import os, time, keyboard 

start_page = 1
total_page = 710
book_name = 'principle'
top_x = 1803
top_y = -937
end_x = 2682
end_y = 169 
roi = (top_x, top_y,  abs(end_x-top_x), abs(end_y-top_y))
ebook_screen_next_page =(2720,-390)
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
        time.sleep(3)

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
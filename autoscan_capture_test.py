import pyautogui
import time

# ---  마우스 좌표 구하기
for i in range(10):
    time.sleep(3)
    print(f"{i}th : {pyautogui.position()}")


# ---  화면 size
# print(pyautogui.size ())
# --- 커서 위치
cursor_position = pyautogui.position()
# Define the region of interest (roi)
top_x = 1803
top_y = -937
end_x = 2682
end_y = 169 

roi = (top_x,top_y,  abs(end_x-top_x), abs(end_y-top_y))
# Capture the screen
screenshot = pyautogui.screenshot(region=roi)

# Save the image
screenshot.save('./data/screenshot.png')


ebook_screen_next_page =(2720,-390)
pyautogui.doubleClick(ebook_screen_next_page)
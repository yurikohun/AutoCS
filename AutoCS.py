import pyautogui
import time
import win32api
from python_imagesearch.imagesearch import imagesearch

while True:
    print("Choose resolution.")
    print("1.: 1920x1080")
    print("2.: 1280x1024")
    print("3.: Exit")
    x = int(input())
    if x > 3:
        print("This isn't an option.")
        time.sleep(3)
    elif x < 1:
        print("This isn't an option.")
        time.sleep(3)
    elif x == 1:
        while True:
            pos = imagesearch("accept19201080.png")
            if pos[0] != -1:
                x, y = pyautogui.locateCenterOnScreen("accept19201080.png")
                win32api.SetCursorPos((x, y))
                pyautogui.leftClick()
                break
    elif x == 2:
        while True:
            pos = imagesearch("accept19201080.png")
            if pos[0] != -1:
                x, y = pyautogui.locateCenterOnScreen("accept19201080.png")
                win32api.SetCursorPos((x, y))
                pyautogui.leftClick()
                break
    elif x == 3:
        exit()

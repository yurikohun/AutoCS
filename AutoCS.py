import pyautogui
import python_imagesearch
from python_imagesearch.imagesearch import (imagesearch)
from PIL import Image
import time

while True:
    print("Válassz felbontást.")
    print("1.: 1920x1080")
    print("2.: 1280x1024")
    print("3.: Bezárás")
    x = int(input())
    if x > 3:
        print("Ez nem egy lehetőség.")
        time.sleep(3)
    elif x < 1:
        print("Ez nem egy lehetőség.")
        time.sleep(3)
    elif x == 1:
        while True:
            pos = imagesearch("fullhd169.png")
            if pos[0] != -1:
                print("position : ", pos[0], pos[1])
                pyautogui.moveTo(pos[0], pos[1])
                pyautogui.leftClick()
                break
    elif x == 2:
        while True:
            pos = imagesearch("1280x1024.png")
            if pos[0] != -1:
                print("position : ", pos[0], pos[1])
                pyautogui.moveTo(pos[0], pos[1])
                pyautogui.leftClick()
                break
    elif x == 3:
        exit()
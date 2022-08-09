from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con

time.sleep(2)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


timesClicked = 0

while keyboard.is_pressed('q') == False:
    pic = pyautogui.screenshot(region=(530, 375, 600, 400))
    width, hieght = pic.size

    for x in range(0, width, 5):
        for y in range(0, hieght, 5):
            r, g, b = pic.getpixel((x, y))

            if b == 195:
                click(x+530, y+375)
                time.sleep(0.05)
                timesClicked += 1
                print(f"Clicked {timesClicked} times")
                break

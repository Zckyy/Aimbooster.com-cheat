#This file grabs the region of your screen and saves at as a png in the base directory.

import pyautogui

im1 = pyautogui.screenshot(region=(530,375,600,400))
im1.save(r"my_screenshot.png")
from pyautogui import *
import pyautogui
import keyboard
import time
import random
import win32con, win32api

time.sleep(3)

#color = (255, 219, 195)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q')==False:
    pic = pyautogui.screenshot(region=(658,336,604,422))
    width,height = pic.size

    for x in range(0,width,5):
        for y in range(0,height,5):
            r,g,b = pic.getpixel((x,y))
            if b==195:
                click(x+658,y+336)
                time.sleep(0.1)
                break

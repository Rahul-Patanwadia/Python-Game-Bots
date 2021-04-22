from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#X:  750 Y:  400 RGB: ( 84,  87, 116)
#X:  867 Y:  400 RGB: (  0,   0,   0)
#X: 1024 Y:  400 RGB: ( 80,  83, 116)
#X: 1193 Y:  400 RGB: ( 85,  87, 116)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q')==False:
    if pyautogui.pixel(750,400)[0]==0:
        click(750,400)
    if pyautogui.pixel(867,400)[0]==0:
        click(867,400)
    if pyautogui.pixel(1024,400)[0]==0:
        click(1024,400)
    if pyautogui.pixel(1193,400)[0]==0:
        click(1193,400)
    

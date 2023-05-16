from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import sys


sys.platform = '_'
pyautogui.displayMousePosition()

#X: 2553 Y:  607 RGB: (NaN, NaN, NaN)
#X: 2661 Y:  613 RGB: (NaN, NaN, NaN)
#X: 2713 Y:  613 RGB: (NaN, NaN, NaN)
#X: 2810 Y:  617 RGB: (NaN, NaN, NaN)

def click(x,y):

    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(2553, 607)[0] == 0:
        click(2553,607)
    if pyautogui.pixel(2661, 607)[0] == 0:
        click(2661,607)
    if pyautogui.pixel(2713, 607)[0] == 0:
        click(2713,607)
    if pyautogui.pixel(2810, 607)[0] == 0:
        click(2810,607) 

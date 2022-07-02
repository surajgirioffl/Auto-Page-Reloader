"""
    Script to auto reload a webpage by pressing ctrl + r.
    Used of external module pyautogui.
"""
from pyautogui import hotkey
from time import sleep
i = 0
while(i <= 1000):
    if(i == 0):
        sleep(5)  # to sleep for 5 seconds
    hotkey("ctrl", "r")

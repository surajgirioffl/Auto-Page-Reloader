"""
    Script to auto reload a webpage by pressing ctrl + r every second.
    Used of external module pyautogui.
     *author: Suraj Kumar Giri.
     *Date: 06-07-2022 (Last Updated)
     *Time: 12:48:20
"""
from pyautogui import hotkey
from time import sleep
# to sleep for 5 seconds for switching to respective webpage to implement the script
sleep(5)

while(True):
    hotkey("ctrl", "r")
    # sleep(0.3)

'''from pynput.keyboard import Key, Controller
import pyautogui
keyboard = Controller()

# Press and release special key 

# Press and release normal key 
#keyboard.press('a')
keyboard.press(ENTER)
'''
'''import win32com.client
 
shell = win32com.client.Dispatch("WScript.Shell")
shell.SendKeys("{ENTER}") # CTRL+A may "select all" depending on which window's focused
#shell.SendKeys("{DELETE}") # Delete selected text?  Depends on context. :P

#shell.SendKeys("{TAB}") #Press tab... to change focus or whatever
'''
import pyautogui, sys
import time
pyautogui.position()
a = pyautogui.position()
print(a)
s = input("nhap: ")
#time.sleep(4)
while True:
    if s == 'c':
       time.sleep(4)
       pyautogui.moveTo(22, 1054)
       pyautogui.click(button='left')
       s = input("nhap: ")
    if s == 'q':
        break
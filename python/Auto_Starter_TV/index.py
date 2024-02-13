import pyautogui
import os
x=734
y=767

pyautogui.moveTo(x,y)
pyautogui.click()
x=596 
y=467
pyautogui.moveTo(x,y)
pyautogui.sleep(1)
pyautogui.click()
x=683
y=66
pyautogui.moveTo(x,y)
pyautogui.click()

pyautogui.typewrite("www.bing.com")
pyautogui.press("enter")

os.system("shutdown /s /t 1")

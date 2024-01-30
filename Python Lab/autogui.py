import pyautogui
import time

path="D:/5th Sem/Advance Python/Practical - Theory/Pyautogui/pyautoguidemo.txt"
pyautogui.press('win')
time.sleep(2)
pyautogui.write('chrome')
time.sleep(5)
pyautogui.press('enter')
time.sleep(2)
pyautogui.hotkey('shift','tab')
pyautogui.hotkey('shift','tab')
pyautogui.hotkey('shift','tab')
pyautogui.hotkey('shift','tab')
pyautogui.hotkey('shift','tab')
pyautogui.hotkey('shift','tab')
pyautogui.hotkey('shift','tab')
pyautogui.hotkey('shift','tab')
pyautogui.hotkey('shift','tab')
time.sleep(1)
pyautogui.press('enter')
time.sleep(2)
pyautogui.write("https://docs.google.com/document/create")
time.sleep(5)
pyautogui.press('enter')
time.sleep(10)
pyautogui.press('win')
time.sleep(2)
pyautogui.write("D:\Fifth Sem\Advance Python\Practical - Theory\Pyautogui\pyautoguidemo.txt")
time.sleep(5) 
pyautogui.press('enter')
time.sleep(2)


pyautogui.keyDown('alt')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.keyUp('alt')




time.sleep(2)

pyautogui.hotkey('ctrl','a')
pyautogui.hotkey('ctrl','c')
time.sleep(2)
pyautogui.hotkey('alt','tab') 
time.sleep(2)
pyautogui.hotkey('ctrl','v')
import pyautogui
import time
import csv

path = "D:\\COLLEGE\\Python Lab\\Theory\\Assignment-2\\"

pyautogui.hotkey('win', 'r')
time.sleep(2)

pyautogui.write(path + 'data.txt')
pyautogui.press('enter')
time.sleep(2)

pyautogui.hotkey('ctrl', 'a')
time.sleep(2)

pyautogui.hotkey('ctrl', 'c')
time.sleep(2)

pyautogui.hotkey('win', 'r')
time.sleep(2)

pyautogui.write('notepad')
pyautogui.press('enter')
time.sleep(2)

pyautogui.hotkey('ctrl', 'v')
time.sleep(2)

pyautogui.hotkey('ctrl', 's')
time.sleep(2)

for i in range(7):
    pyautogui.press('tab')
    time.sleep(2)

pyautogui.press('enter')
time.sleep(2)

pyautogui.write(path)
time.sleep(2)

pyautogui.press('enter')
time.sleep(2)

for i in range(6):
    pyautogui.press('tab')
    time.sleep(2)

pyautogui.write('output.csv')
time.sleep(2)

for i in range(4):
    pyautogui.press('tab')
    time.sleep(2)

pyautogui.press('enter')
time.sleep(2)

data = []

with open('output.csv', 'r') as f:
    for line in f.readlines():
        fields = line.strip().split(',')
        data.append(fields)
    totalReviews = len(data) - 1
    totalFields = len(data[0])
    print("Total reviews: ", totalFields)
    print("Total fields: ", totalFields)

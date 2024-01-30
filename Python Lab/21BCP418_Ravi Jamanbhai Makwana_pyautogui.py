import pyautogui
import time

google_docs_url = 'https://docs.google.com/'
file_path = 'D:\\COLLEGE\\Python Lab\\Theory\\auto.txt'

# Read and copy the content of the text file
with open(file_path, 'r') as file:
    file_content = file.read()

# copy to clipboard
pyautogui.write(file_content)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
time.sleep(2)


# Open Google Docs
pyautogui.hotkey('ctrl', 't')
pyautogui.typewrite(google_docs_url)
pyautogui.press('enter')
time.sleep(5)

pyautogui.click(x=500, y=500)
time.sleep(5)

pyautogui.hotkey('ctrl', 'v')  # Paste the copied text

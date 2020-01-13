import pyautogui

print(pyautogui.position())
print(pyautogui.size())
print(pyautogui.PAUSE)

x, y = pyautogui.size()
pyautogui.moveTo(x / 2, y / 2, duration=3)

print(pyautogui.screenshot())

print(pyautogui.locateOnScreen('file.png'))
list(pyautogui.locateAllOnScreen('looksLikeThis.png'))


import pyautogui

# x, y = pyautogui.size()
# print(x, y)

start_pos = (0, 0)
while True:
    if start_pos == pyautogui.position():
        continue
    start_pos = pyautogui.position()
    print(start_pos)
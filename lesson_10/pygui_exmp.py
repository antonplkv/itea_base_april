import pyautogui

pyautogui.FAILSAFE = False

# lesson_3_coordinates = (1601, 47)
# pyautogui.moveTo(lesson_3_coordinates[0], lesson_3_coordinates[1], 3)
#pyautogui.moveRel(-500, 600, 1)

pyautogui.moveTo(886, 206, 3)
pyautogui.dragRel(xOffset=-400, duration=1)
pyautogui.hotkey('ctrl', 'c')
pyautogui.moveRel(yOffset=350, xOffset=20, duration=1)
pyautogui.click()
pyautogui.hotkey('ctrl', 'v')
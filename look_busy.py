#Simple program that automatically nudges the mouse when away from computer

import pyautogui
import time

def check_mouse_movement():
	xold, yold = pyautogui.position()
	time.sleep(10)
	if xold, yold != pyautogui.position():
		return False
	else:
		return True

while True:
	if not check_mouse_movement():
		pyautogui.moveRel(10, 0, duration = 0.1)
		pyautogui.moveRel(-10, 0, duration = 0.1)


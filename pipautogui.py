import pyautogui
import time

pyautogui.PAUSE = 0.3

#pegar posiçao do mose da tela
print(pyautogui.position())
print(pyautogui.size())

#funçao do mouse
time.sleep(5)
#pyautogui.click(x=617, y=111 )
pyautogui.moveTo(x=968, y=243, duration=1)
pyautogui.click(x=805, y=627)
pyautogui.scroll()
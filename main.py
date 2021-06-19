import pyautogui
from pynput.keyboard import Key, Listener
pyautogui.useImageNotFoundException()

def on_press(key):
    if(key.char=="`"):
        try:
            location = pyautogui.locateOnScreen('bobber.png',grayscale=True,confidence=.6)
            bobberX, bobberY = pyautogui.center(location)
            pyautogui.rightClick(bobberX, bobberY)
        except pyautogui.ImageNotFoundException:
            print("not found")




with Listener(on_press=on_press) as listener:
    listener.join()



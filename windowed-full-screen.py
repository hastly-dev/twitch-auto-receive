import pyautogui
import keyboard
import time
import threading

posX = 1692
posY = 1021

if pyautogui.size() == (2560, 1440):
    posX = 2256
    posY = 1362
elif pyautogui.size() == (3840, 2160):
    posX = 3384
    posY = 2042
elif pyautogui.size() == (7680, 4320):
    posX = 6768
    posY = 4084

exit = False

def check():
    global exit
    while True:
        if keyboard.is_pressed("right ctrl"):
            exit = True
            print("Shutting down...")
            break

def scanning():
    while exit == False:
        screen = pyautogui.screenshot()
        print("Scanning...")
        if screen.getpixel((posX, posY)) == (0,219,132):
            pyautogui.click(posX, posY)
            print("Points received!")
            pyautogui.moveTo(posX-240, posY-320)
        
        time.sleep(5)


if __name__ == '__main__':
    threading.Thread(target=scanning).start()
    threading.Thread(target=check).start()

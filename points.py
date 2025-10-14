import pyautogui
import keyboard
import time
import threading

print("Hover your mouse over the green area or potential green area of the points button and press the <Right Alt> key.")
keyboard.wait('right alt')
posX, posY = pyautogui.position()

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
        print("...")
        if screen.getpixel((posX, posY)) == (0,219,132):
            pyautogui.click(posX, posY)
            print("Points received!")
        
        time.sleep(5)


if __name__ == '__main__':
    threading.Thread(target=scanning).start()
    threading.Thread(target=check).start()
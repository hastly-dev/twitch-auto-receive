import pyautogui
import keyboard
import time
import threading

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
        print("Screenshot")
        if screen.getpixel((1692, 1021)) == (0,219,132):
            pyautogui.click(1692, 1021)
            print("Points received!")
        
        time.sleep(5)
        scanning()


if __name__ == '__main__':
    threading.Thread(target=scanning).start()
    threading.Thread(target=check).start()

# x = 1692, y = 1021, hex = #00db84, rgb = rgb(0 219 132)
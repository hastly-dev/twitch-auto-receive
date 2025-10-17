# Twitch Auto Receive
### Automating the collection of channel points for watching on twitch.
> **Note:** The screen size of the main monitor must be at least 1920x1080.

### 📁 **Libraries**
- pyautogui
- keyboard
- _time_
- _threading_
## ℹ️ **How to use**
### Released version
- Download the latest released version on https://github.com/hastly-dev/twitch-auto-receive/releases
- Open `adaptive.exe` or `windowed-full-screen.exe`
- Use the **Right Ctrl** key to stop the program.
> If you have chosen `adaptive.exe`, you need to hover the mouse cursor over the green area or the potential green area of the points button and press the Right Alt key.
### Using the source code
- Download all the required libraries using `pip install`
- Open in PyCharm or CMD using `python adaptive.py` or `python windowed-full-screen.py`
- Use the **Right Ctrl** key to stop the program.
## ℹ️ **How it works**
Every 5 seconds, the program takes a screenshot of the screen, and on this screenshot it searches for a pixel of color rbg(0,219,132). If such a pixel is on the screenshot (on the screen), then this pixel is clicked.
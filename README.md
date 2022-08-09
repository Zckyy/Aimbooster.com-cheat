
# Aimbooster.com-cheat

Scans every 5th pixel on a defined region. On every 5th pixel it checks the blue channel of RGB values for the value of 195.
Once finding a match, it will invoke a click using pywin32 library.

You have 2 seconds from opening the script to start a game on Aimbooster.com, make sure the window is focused and it should start clicking each target.

Pyhon setup
---
Install these libraries from an administrator terminal (windows):

- pip install pywin32
- pip install keyboard
- pip install pyautogui
- pip install opencv-python

Make sure you are running the latest version of Python.

Screen region setup
---
This is a pixelbot, so you will need to configure the region of screen capture manually. Fortunately this is not too difficult.

Open the [region.py](https://github.com/Zckyy/Aimbooster.com-cheat/blob/master/region.py) file in a text editor. Within this file you will need to configure the paramaters of region to fit the game window of Aimbooster.com. By default the values are set already to what works for me.

    (region=(530,375,600,400))

The first and second value is the x,y position of the region on the screen, the third and forth values are width and height of that region.

Keep saving the file each time you make changes to the region size, and you will see the output in the folder where the scripts live.

once you have configured the region size, and have a screenshot that looks something simlar to the one below you can continue!

![enter image description here](https://i.imgur.com/cyqNxzc.png)

Inputting your configured into the main file
---
Now that you have configured your capture region, you can input these values into the main.py file.

**Firstly**, add your region sizes to the line below:

    pic = pyautogui.screenshot(region=(yourValues,  yourValues,  yourValues,  yourValues))

**Secondly**, add your first two region size values to the following line:

    click(x+yourValues, y+yourValues)

For example if your values were: 435, 560, 230, 300. Your code would look like:

    pic = pyautogui.screenshot(region=(435,  560,  230,  300))
AND
a
    click(x+435, y+560)

Save the file. Open up a aimbooster.com session, run the python file, and put the aimbooster.com window on focus. Do not block the viewing area of the game otherwise the bot will fail to pick up the targets.

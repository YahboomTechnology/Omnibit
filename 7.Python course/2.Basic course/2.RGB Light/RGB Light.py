from microbit import *
import neopixel

np = neopixel.NeoPixel(pin12, 4)
display.show(Image.HAPPY)


def RGB_Scintillation(first, num):
    global np
    np.clear()
    while first <= num:
        np.clear()
        np[0] = (255, 0, 0)
        np[1] = (255, 0, 0)
        np[2] = (255, 0, 0)
        np[3] = (255, 0, 0)
        np.show()
        sleep(500)
        np.clear()
        np.show()
        sleep(500)
        first += 1
    else:
        first = 0

    np.show()

def RGB_Waterlamp(first, num):
    global np
    np.clear()
    while first <= num:
        np[0] = (255, 0, 0)
        np.show()
        sleep(200)
        np[1] = (255, 0, 0)
        np.show()
        sleep(200)
        np[2] = (255, 0, 0)
        np.show()
        sleep(200)
        np[3] = (255, 0, 0)
        np.show()
        sleep(200)
        np.clear()
        sleep(200)
        first += 1

def RGB_marquee(first, num):
    global np
    np.clear()
    while first <= num:
        np[0] = (255, 0, 0)
        np.show()
        sleep(200)
        np.clear()
        np[1] = (0, 255, 0)
        np.show()
        sleep(200)
        np.clear()
        np[2] = (0, 0, 255)
        np.show()
        sleep(200)
        np.clear()
        np[3] = (255, 255, 0)
        np.show()
        sleep(200)
        np.clear()
        first += 1

def RGB_Breathinglamp(first, num):
    global np
    np.clear()
    while first <= num:
        for num1 in range(255, 0, -20):
            for pixel_id in range(0, len(np)):
                np[pixel_id] = (num1, 0, num1)    # purple
                np.show()
                sleep(5)
                # RGB lights are changed gradually from light to dark
        for num1 in range(0, 255, 20):
            for pixel_id in range(0, len(np)):
                np[pixel_id] = (num1, 0, num1)   # purple
                np.show()
                sleep(5)
        first += 1

while True:
    RGB_Scintillation(1, 3)
    RGB_Waterlamp(1, 3)
    RGB_marquee(1, 3)
    RGB_Breathinglamp(1, 3)
    sleep(500)
    np.clear()
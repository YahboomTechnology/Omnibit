from microbit import *
import music


def Merry_Christmas():
    tune = ["C4:4", "D4:4", "E4:4", "C4:4", "C4:4", "D4:4", "E4:4", "C4:4",
            "E4:4", "F4:4", "G4:8", "E4:4", "F4:4", "G4:8"]
    music.play(tune)

display.show(Image.HAPPY)
Merry_Christmas()
sleep(2000)
music.play(music.ODE)

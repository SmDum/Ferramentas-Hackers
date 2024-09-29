#python -m pip install pynput

from pynput.mouse import Controller
from pynput.keyboard import Controller

def controlMouse():
    mouse = Controller()
    mouse.position = (500,200)

def controlKeyboard():
    keyboard = Controller()
    keyboard.type("I am Freaking awesome!")

#controlMouse()
#controlKeyboard()

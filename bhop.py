import keyboard
import winsound
import time
import tkinter
from tkinter import *

window = Tk()

window.title("CS:GO Bhop-Script Python")

window.geometry('350x200')

lbl = Label(window, text="Click here to Start -->")

lbl.grid(column=0, row=0)

def bhop():
    while True:
        if keyboard.is_pressed('space'):
            keyboard.press_and_release('space')
            time.sleep(0.05)

def clicked():
    winsound.Beep(1000, 200)
    bhop()
23
btn = Button(window, text="UwU" , command = clicked)

btn.grid(column=1, row=0)
window.mainloop()

        


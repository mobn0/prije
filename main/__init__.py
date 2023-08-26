import pygame
import screeninfo as si
import tkinter


root = tkinter.Tk()
root.withdraw()
WIDTH, HEIGHT = root.winfo_screenwidth(), root.winfo_screenheight()
for x in si.get_monitors():
    print(x)

print("lopöpökpiolüäöüäpüüpö")
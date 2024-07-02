import tkinter as tk
from tkinter import colorchooser

def pen():
    global x
    x = "pen"
def brush():
    global x
    x = "brush"
def coloring():
    color = colorchooser.askcolor()
    if color[0]:
        global pen_co
        pen_co = color[1]
def eraser():
    global x
    x = "eraser"
def size(n):
    global pen_s
    pen_s = int(n)

def paint(a):
    x1,y1 = (a.x -pen_s),(a.y - pen_s)
    x2,y2 = (a.x + pen_s),(a.y + pen_s)

    if x == "pen":
        canvas.create_oval(x1,y1,x2,y2,fill=pen_co,width=s)

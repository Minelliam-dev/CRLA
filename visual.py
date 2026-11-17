import tkinter as tk
from ai import *


win = tk.Tk()
win.geometry("1000x500")
win.title("visualisation")

canvas = tk.Canvas(win, width=1000, height=500, bg="#000000")
canvas.pack()

options = ["-2", "-1", "0", "1", "2"]
rewards = [-2, -1, 0, 1, 2]

VisualValue = 1

ai = AI(options, rewards)


i=0

while True:
    i += .1
    
    ai.pickOption()

    AIValue = (-(ai.chances[VisualValue]) + 225)

    if (i<1000): canvas.create_line(i, AIValue, i-1, AIValue, fill="#ffffff")

    win.update()
    
    if not (win.winfo_exists()): break
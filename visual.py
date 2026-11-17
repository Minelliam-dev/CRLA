import tkinter as tk
from ai import *


win = tk.Tk()
win.geometry("1002x522")
win.title("visualisation")
win.config(bg="#000000")


canvas = tk.Canvas(win, width=1000, height=500, bg="#232323")
canvas.place(x=0, y=20)

options = ["-2", "-1", "0", "1", "2"]
rewards = [-2, -1, 0, 1, 2]

VisualValue = 1

ai = AI(options, rewards)

i=0
colours = ["#ff0000", "#00ff00", "#ffff00", "#0000ff", "#ff00ff", "#00ffff", "#ffffff"]

while True:
    i += .1
    
    ai.pickOption()

    for c in range(5):
        AIValue = (-(ai.chances[c]/5) + 225)
        if (c<1000): canvas.create_line(i, AIValue, i-1, AIValue, fill=colours[c])

    win.update()
    
    if not (win.winfo_exists()): break
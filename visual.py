import tkinter as tk
from ai import *

LabelText = "2500\n\n\n\n\n\n\n\n\n\n\n+0\n-0\n\n\n\n\n\n\n\n\n\n\n\n\n-2500"

win = tk.Tk()
win.geometry("1052x522")
win.title("visualization")
win.config(bg="#000000")

canvas = tk.Canvas(win, width=1000, height=500, bg="#232323")
canvas.place(x=0, y=20)

text = tk.Label(win, text=LabelText, fg="#ffffff", bg="#232323")
text.place(x=1002, y=20)

colours = ["#ff0000", "#00ff00", "#ffff00", "#0000ff", "#ff00ff", "#00ffff", "#ffffff"]
options = ["1", "2", "3", "4", "5"]
rewards = [-2, -1, 0, 1, 2]

ai = AI(options, rewards)

i=0
while True:
    i += .1
    
    ai.pickOption()

    for c in range(5):
        AIValue = (-(ai.chances[c]/5) + 225)
        if (c<1000): canvas.create_line(i, AIValue, i-1, AIValue, fill=colours[c])

    win.update()
    
    try:
        win.winfo_exists()
    except:
        break
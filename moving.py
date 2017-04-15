import time
from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=400, height=200)
canvas.pack()
canvas.create_polygon(10,10,10,60,50,35)

while True:
    for x in range(0,200):
        canvas.move(1,1,0)
        tk.update()
        time.sleep(0.01)
    for y in range(0,200):
        canvas.move(1,-1,0)
        tk.update()
        time.sleep(0.01)

import math
from tkinter import *
root = Tk()
myCanvas = Canvas(root)
myCanvas.pack()
myCanvas.config(width=1920, height=1080)
root.geometry("1920x1080")

def create_circle(x, y, r, canvasName): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1)



def plot_pixel(x, y, canvasName):
    return create_circle(x, y, 0, canvasName)

corna = 7
cornb = 3
side = 20

for i in range(1024):
    for j in range(576):
        x = corna + i * side/100
        y = cornb + j * side/100
        c = math.floor(x * x + y * y)
        if c % 2 == 0:
            plot_pixel(i, j, myCanvas)

root.mainloop()
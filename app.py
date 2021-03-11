from tkinter import *

graphic = Tk()
graphic.title("Calculator")

display = Entry(graphic)
display.grid(row=1, columnspan=6, sticky=W+E)

# number buttons
Button(graphic, text=1,).grid(row=2)

graphic.mainloop()
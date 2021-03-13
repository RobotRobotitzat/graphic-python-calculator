from tkinter import *

graphic = Tk()
graphic.title("Calculator")

display = Entry(graphic)
display.grid(row=1, columnspan=6, sticky=W+E)

# grapic code

# number buttons row one 
Button(graphic, text="1").grid(row=2, column=0, sticky=W+E)
Button(graphic, text="2").grid(row=2, column=1, sticky=W+E)
Button(graphic, text="3").grid(row=2, column=2, sticky=W+E)

# number buttons row two
Button(graphic, text="4").grid(row=3, column=0, sticky=W+E)
Button(graphic, text="5").grid(row=3, column=1, sticky=W+E)
Button(graphic, text="6").grid(row=3, column=2, sticky=W+E)

# number buttons row three
Button(graphic, text="7").grid(row=4, column=0, sticky=W+E)
Button(graphic, text="8").grid(row=4, column=1, sticky=W+E)
Button(graphic, text="9").grid(row=4, column=2, sticky=W+E)

# number buttons row five
Button(graphic, text="0").grid(row=5, column=1, sticky=W+E)


# other buttons

Button(graphic, text="AC").grid(row=5, column=2, sticky=W+E)
Button(graphic, text="%").grid(row=5, column=0, sticky=W+E)

Button(graphic, text="←").grid(row=2, column=4, sticky=W+E, columnspan=2)
Button(graphic, text="EXP").grid(row=3, column=4, sticky=W+E)
Button(graphic, text="^2").grid(row=3, column=5, sticky=W+E)
Button(graphic, text="(").grid(row=4, column=4, sticky=W+E)
Button(graphic, text=")").grid(row=4, column=5, sticky=W+E)
Button(graphic, text="=").grid(row=5, column=4, sticky=W+E, columnspan=2)

# operation buttons
Button(graphic, text="+").grid(row=2, column=3, sticky=W+E)
Button(graphic, text="-").grid(row=3, column=3, sticky=W+E)
Button(graphic, text="*").grid(row=4, column=3, sticky=W+E)
Button(graphic, text="/").grid(row=5, column=3, sticky=W+E)


# code
index = 0

def get_numbers(n):
    display.insert(i, n)
    index +=1


# mainloop
graphic.mainloop()
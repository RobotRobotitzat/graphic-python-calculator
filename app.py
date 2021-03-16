from tkinter import *
import parser

graphic = Tk()
graphic.title("Calculator")

display = Entry(graphic)
display.grid(row=1, columnspan=6, sticky=W+E)

# grapic code

# number buttons row one 
Button(graphic, text="1", command=lambda:get_numbers("1")).grid(row=2, column=0, sticky=W+E)
Button(graphic, text="2", command=lambda:get_numbers("2")).grid(row=2, column=1, sticky=W+E)
Button(graphic, text="3", command=lambda:get_numbers("3")).grid(row=2, column=2, sticky=W+E)

# number buttons row two
Button(graphic, text="4", command=lambda:get_numbers("4")).grid(row=3, column=0, sticky=W+E)
Button(graphic, text="5", command=lambda:get_numbers("5")).grid(row=3, column=1, sticky=W+E)
Button(graphic, text="6", command=lambda:get_numbers("6")).grid(row=3, column=2, sticky=W+E)

# number buttons row three
Button(graphic, text="7", command=lambda:get_numbers("7")).grid(row=4, column=0, sticky=W+E)
Button(graphic, text="8", command=lambda:get_numbers("8")).grid(row=4, column=1, sticky=W+E)
Button(graphic, text="9", command=lambda:get_numbers("9")).grid(row=4, column=2, sticky=W+E)

# number buttons row five
Button(graphic, text="0", command=lambda:get_numbers("0")).grid(row=5, column=1, sticky=W+E)


# other buttons

Button(graphic, text="AC", command=lambda:clear_calculator()).grid(row=5, column=2, sticky=W+E)
Button(graphic, text="%", command=lambda:get_operations("%")).grid(row=5, column=0, sticky=W+E)

Button(graphic, text="←", command=lambda:undo()).grid(row=2, column=4, sticky=W+E, columnspan=2)
Button(graphic, text="EXP", command=lambda:get_operations("**")).grid(row=3, column=4, sticky=W+E)
Button(graphic, text="^2", command=lambda:get_operations("**2")).grid(row=3, column=5, sticky=W+E)
Button(graphic, text="(", command=lambda:get_operations("(")).grid(row=4, column=4, sticky=W+E)
Button(graphic, text=")", command=lambda:get_operations(")")).grid(row=4, column=5, sticky=W+E)
Button(graphic, text="=", command=lambda:result()).grid(row=5, column=4, sticky=W+E, columnspan=2)

# operation buttons
Button(graphic, text="+", command=lambda:get_operations("+")).grid(row=2, column=3, sticky=W+E)
Button(graphic, text="-", command=lambda:get_operations("-")).grid(row=3, column=3, sticky=W+E)
Button(graphic, text="*", command=lambda:get_operations("*")).grid(row=4, column=3, sticky=W+E)
Button(graphic, text="/", command=lambda:get_operations("/")).grid(row=5, column=3, sticky=W+E)


# code
index = 0

# numbers commands
def get_numbers(n):
    global index
    display.insert(index, n)
    index +=1

# operations command
def get_operations(operator):
    global index
    operator_len = len(operator)
    display.insert(index, operator)
    index+=operator_len

# clear
def clear_calculator():
    display.delete(0, END)

# undo
def undo():
    display_status = display.get()
    if len(display_status):
        display_status_new = display_status[:-1]
        clear_calculator()
        display.insert(0, display_status_new)
    else:
        clear_calculator()
        display.insert(0, "ERROR")

# result
def result():
    display_status = display.get()
    try:
        expression = parser.expr(display_status).compile()
        result_operation = eval(expression)
        clear_calculator()
        display.insert(0, result_operation)
    except expression as identifier:
        clear_calculator()
        display.insert(0, "Syntax ERROR")

# mainloop
graphic.mainloop()
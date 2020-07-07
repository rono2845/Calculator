from tkinter import *
import parser

root = Tk()
root.title("Calculator")
#get the user input and place it into the input box
i=0
def takeInput(number):
   global i
   display.insert(i, number)
   i += 1

def takeOperation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length

#for = button
def compute():
   entire_string = display.get()
   try:
       a = parser.expr(entire_string).compile()
       result = eval(a)
       clearAll()
       display.insert(0, result)
   except Exception:
       clearAll()
       display.insert(0, "Error")

#for AC button
def clearAll():
    display.delete(0, END)

#for <-- button
def clearSingle():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1] #list slicing
        clearAll()
        display.insert(0, new_string)
    else:
        clearAll()
        display.insert(0, "Error")


#adding the input field
display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E)

#adding the button(numbers) in Calculator

Button(root, text="1", bg="orange", command=lambda :takeInput(1)).grid(row=2, column=0, padx=1, pady=5)
Button(root, text="2", bg="orange", command=lambda :takeInput(2)).grid(row=2, column=1, padx=1, pady=5)
Button(root, text="3", bg="orange", command=lambda :takeInput(3)).grid(row=2, column=2, padx=1, pady=5)

Button(root, text="4", bg="orange", command=lambda :takeInput(4)).grid(row=3, column=0, padx=1, pady=5)
Button(root, text="5", bg="orange", command=lambda :takeInput(5)).grid(row=3, column=1, padx=1, pady=5)
Button(root, text="6", bg="orange", command=lambda :takeInput(6)).grid(row=3, column=2, padx=1, pady=5)

Button(root, text="7", bg="orange", command=lambda :takeInput(7)).grid(row=4, column=0, padx=1, pady=5)
Button(root, text="8", bg="orange", command=lambda :takeInput(8)).grid(row=4, column=1, padx=1, pady=5)
Button(root, text="9", bg="orange", command=lambda :takeInput(9)).grid(row=4, column=2, padx=1, pady=5)

#adding the button(basic operation) in Calculator

Button(root, text="AC", bg="red", command=lambda :clearAll()).grid(row=5, column=0, padx=1, pady=5)
Button(root, text="0", bg="orange", command=lambda :takeInput(0)).grid(row=5, column=1, padx=1, pady=5)
Button(root, text="=", bg="green", command=lambda :compute()).grid(row=5, column=2, padx=1, pady=5)

Button(root, text="+", bg="green", command= lambda :takeOperation('+')).grid(row=2, column=3, padx=1, pady=5)
Button(root, text="-", bg="green", command= lambda :takeOperation('-')).grid(row=3, column=3, padx=1, pady=5)
Button(root, text="*", bg="green", command= lambda :takeOperation('*')).grid(row=4, column=3, padx=1, pady=5)
Button(root, text="/", bg="green", command= lambda :takeOperation('/')).grid(row=5, column=3, padx=1, pady=5)


#adding the button(special operation) in Calculator

Button(root, text="π", bg="green", command=lambda :takeOperation("*3.141")).grid(row=2, column=4, padx=1, pady=5)
Button(root, text="(", bg="green", command=lambda :takeOperation("(")).grid(row=3, column=4, padx=1, pady=5)
Button(root, text="exp", bg="green", command=lambda :takeOperation("**")).grid(row=4, column=4, padx=1, pady=5)

Button(root, text="<--", bg="green", command=lambda :clearSingle()).grid(row=2, column=5, padx=1, pady=5)
Button(root, text=")", bg="green", command=lambda :takeOperation(")")).grid(row=3, column=5, padx=1, pady=5)
Button(root, text="x^2", bg="green", command=lambda :takeOperation("**2")).grid(row=4, column=5, padx=1, pady=5)

root.mainloop()
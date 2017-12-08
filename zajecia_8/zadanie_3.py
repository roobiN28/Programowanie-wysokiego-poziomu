from Tkinter import *

first = None

resultAction = None


def clear():
    global first
    global resultAction
    first = None
    resultAction = None
    entry.delete(0, END)


def add():
    global first
    global resultAction
    if first is None:
        first = int(entry.get())
        entry.delete(0, END)
        resultAction = add
    else:
        result = first + int(entry.get())
        entry.delete(0, END)
        entry.insert(0, result)
        first = None
        resultAction = None


def subtract():
    global first
    global resultAction
    if first is None:
        first = int(entry.get())
        entry.delete(0, END)
        resultAction = add
    else:
        result = first - int(entry.get())
        entry.delete(0, END)
        entry.insert(0, result)
        first = None
        resultAction = None


def multiply():
    global first
    global resultAction
    if first is None:
        first = int(entry.get())
        entry.delete(0, END)
        resultAction = add
    else:
        result = first * int(entry.get())
        entry.delete(0, END)
        entry.insert(0, result)
        first = None
        resultAction = None


def divide():
    global first
    global resultAction
    if first is None:
        first = int(entry.get())
        entry.delete(0, END)
        resultAction = add
    else:
        result = first / int(entry.get())
        entry.delete(0, END)
        entry.insert(0, result)
        first = None
        resultAction = None


def result():
    global resultAction
    if resultAction is not None:
        resultAction()
        resultAction = None


root = Tk()

entry = Entry(root)
buttonClear = Button(root, text='C', command=clear)
buttonAdd = Button(root, text='+', command=subtract)
buttonSubtract = Button(root, text='-', command=subtract)
buttonMultiply = Button(root, text='*', command=multiply)
buttonDivide = Button(root, text='/', command=divide)
buttonResult = Button(root, text='=', command=result)

entry.grid(row=0, column=0, columnspan=5)
buttonClear.grid(row=1, column=0)
buttonAdd.grid(row=1, column=1)
buttonSubtract.grid(row=1, column=2)
buttonMultiply.grid(row=1, column=3)
buttonDivide.grid(row=1, column=4)
buttonResult.grid(row=1, column=5)

root.mainloop()

from Tkinter import *
import tkMessageBox

value1 = None

resultAction = None
def add():
    global value1
    global resultAction
    if value1 is None:
        value1 = int(entry.get())
        entry.delete(0,END)
        resultAction = add
    else:
        result = value1 + int(entry.get())
        entry.delete(0,END)
        entry.insert(0,result)
        value1 = None


def result():
    resultAction()

root = Tk()

entry = Entry(root)
button = Button(root, text='+', command=add)
button1 = Button(root, text='=', command=result)


entry.grid(row=0, column=0, columnspan=2)
button.grid(row=1, column=0)
button1.grid(row=1, column=1)

root.mainloop()

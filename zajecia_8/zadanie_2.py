import tkMessageBox
from Tkinter import *

timeToCount = 0
sec = 0


def showInfo():
    tkMessageBox.showinfo('Info', 'Czas minal')


def tick():
    global sec
    sec += 1
    label['text'] = timeToCount - sec
    if timeToCount == sec:
        sec = 0
        label['text'] = ''
        showInfo()
        return
    label.after(1000, tick)


def startTimer():
    global timeToCount
    timeToCount = int(input.get())
    tick()


root = Tk()

input = Entry(root)
input.grid(row=0, column=0)

label = Label(root)
label.grid(row=1, column=0)

button = Button(root, text='Start', command=startTimer)
button.grid(row=2, column=0)

root.mainloop()

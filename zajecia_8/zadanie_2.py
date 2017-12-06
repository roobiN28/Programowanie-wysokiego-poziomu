from Tkinter import *
import tkMessageBox
import time

def showInfo():
    tkMessageBox.showinfo('Info', 'Czas minal')

def startCounting():

    counter = input.get()
    input.insert(0, counter)


root = Tk()

input = Entry(root)
input.grid(row=0, column=0)

label = Label(root)
label.grid(row=1, column=0)
label.grid_remove()

button = Button(root, text='Start', command=startCounting)
button.grid(row=2, column=0)

root.mainloop()

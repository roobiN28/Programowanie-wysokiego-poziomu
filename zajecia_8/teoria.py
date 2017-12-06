from Tkinter import *
import tkFont
import tkMessageBox

def labelConfig(label, txt):
    label.config(text=txt, fg='light green', bg='dark green')

def showInfo(message):
    tkMessageBox.showinfo('Message: ' + message)

root = Tk()
l1 = Label(root, text='Hello Tkinter')
labelConfig(l1, '123')

defaultFont = tkFont.nametofont('TkDefaultFont')
defaultFont.configure(size=48)
root.option_add('*Font', defaultFont)


l2 = Label(root, text='L3', bg='blue')
l3 = Label(root, text='L3', bg='gray')

l1.grid(row=0, column=0, columnspan=2)
l2.grid(row=1, column=0)
l3.grid(row=1, column=1)

Button(root, text='Quit', command=root.quit).grid(row=2, column=0)
root.mainloop()


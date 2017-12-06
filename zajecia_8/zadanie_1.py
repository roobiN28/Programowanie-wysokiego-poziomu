from Tkinter import *
import tkMessageBox


def showInfo():
    tkMessageBox.showinfo('Info', 'Information')


root = Tk()
option = StringVar()
option.set('white')
button = Button(root, text='Button', command=showInfo)
button.grid(row=0, column=0)

radio1 = Radiobutton(root, text="RED", variable=option, value='red',
                     command=lambda: button.configure(bg=option.get()))
radio2 = Radiobutton(root, text="GREEN", variable=option, value='green',
                     command=lambda: button.configure(bg=option.get()))
radio3 = Radiobutton(root, text="BLUE", variable=option, value='blue',
                     command=lambda: button.configure(bg=option.get()))

radio1.grid(row=1, column=0)
radio2.grid(row=1, column=1)
radio3.grid(row=1, column=2)

root.mainloop()

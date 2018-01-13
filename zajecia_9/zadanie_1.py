from Tkinter import *
import logging
first = None
resultAction = None

logging.basicConfig(filename='zadanie_1_logger.log', level=logging.DEBUG)


def clear():
    logging.info('clear')
    global first
    global resultAction
    first = None
    resultAction = None
    entry.delete(0, END)


def add():
    logging.info('add')
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
    logging.info('subtract')
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
    logging.info('multiply')
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
    logging.info('divide')
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
    logging.info('result')
    global resultAction
    if resultAction is not None:
        resultAction()
        resultAction = None
    else:
        logging.error('RESULT IS None')

logging.debug('start creating window')
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
logging.debug('window created')
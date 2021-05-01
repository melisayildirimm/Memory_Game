from tkinter import *
import random
from time import sleep
import tkinter.messagebox

root = Tk()
root.geometry("600x600")
root.title("Memory Game")

topFrame = Frame(root, width=600, height=400, bg="pink")
topFrame.pack()
bottomFrame = Frame(root, width=600, height=200, bg="brown")
bottomFrame.pack(side=BOTTOM)

global numbers
global digits
numbers = []
digits = 5

def checkNumbers():
    global digits
    num = []
    variable = e.get()
    num = [int(i) for i in str(variable)]

    if num == numbers:
        answer = tkinter.messagebox.showinfo('melisa', 'CONGRATS,YOU ARE RIGHT!')
        answer1 = tkinter.messagebox.askquestion('melisa', 'DO YOU WANT TO CONTINUE?')
        if answer1 == "yes":
            digits = digits + 1
            numbers.clear()
            myinit()
        else:
            root.quit()

    else:
        answer = tkinter.messagebox.showinfo('melisa', 'OOPS,YOU ARE WRONG!!')
        answer1 = tkinter.messagebox.askquestion('melisa', 'THE GAME WILL START FROM THE BEGINNING.\nDO YOU WANT TO CONTINUE?')
        if answer1 == "yes":
            digits = 5
            numbers.clear()
            myinit()
        else:
            root.quit()


def getInput():
    global e
    input = Label(bottomFrame, text="Enter the numbers:", bg="green")
    input.place(x=80, y=90)
    e = Entry(bottomFrame, fg="black", bg="SpringGreen2")
    e.place(x=200, y=90)
    button = Button(bottomFrame, text="CLick to Check", command=checkNumbers, bg="SlateBlue3")
    button.place(x=350, y=90)

def myinit():

    for i in range(digits):
        numbers.append(random.randint(0, 9))
        label = Label(topFrame, text=numbers[i], bg="orange", font=(None, 10))
        x_coo = random.randint(1, 590)
        y_coo = random.randint(1, 390)
        label.place(x=x_coo, y=y_coo)
        root.update()
        sleep(1)
        label.place_forget()
    print(numbers)
    getInput()


myinit()
root.mainloop()
import time
import tkinter.ttk as ttk
import tkinter.messagebox as msbox
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("300x300")

def info():
    msbox.showinfo("Alarm", "complete")

def warn():
    msbox.showwarning("Warning", "no seat")

def error():
    msbox.showerror("Error", "error occurs")

def okcancel():
    msbox.askokcancel("Ok cancel", "this is not appropriate seat")

def trycancel():
    msbox.askretrycancel("Try cancel", "temporal error, do you want to try again?")

def yesno():
    msbox.askyesno("Yes no", "Do you really want to buy this seat?")

def yesnocancel():
    response = msbox.askyesnocancel(title=None, message="no save. do you want to quit?")
    if response == 1:
        print("Yes")
    elif response == 0:
        print("No")
    else:
        print("Cancel")

Button(root, command=info, text="Alarm").pack()
Button(root, command=warn, text="Warning").pack()
Button(root, command=error, text="Error").pack()
Button(root, command=okcancel, text="Ok cancel").pack()
Button(root, command=trycancel, text="Try cancel").pack()
Button(root, command=yesno, text="Yes no").pack()
Button(root, command=yesnocancel, text="Yes no cancel").pack()

root.mainloop()
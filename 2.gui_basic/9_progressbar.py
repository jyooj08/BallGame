import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("300x300")

# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10)
# progressbar.pack()

# def btncmd():
#     progressbar.stop()

# btn = Button(root, text="click", command=btncmd)
# btn.pack()

def btncmd2():
    for i in range(1, 101): #1~100
        time.sleep(0.01)

        p_var2.set(i)
        progressbar2.update()
        print(p_var2.get())

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

btn = Button(root, text="click", command=btncmd2)
btn.pack()

root.mainloop()
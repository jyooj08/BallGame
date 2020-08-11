from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("300x300")

checkvar = IntVar()
checkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=checkvar)
checkbox.pack()

checkvar2 = IntVar()
checkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=checkvar2)
checkbox2.pack()

def btncmd():
    print(checkvar.get())
    print(checkvar2.get())

btn = Button(root, text="click", command=btncmd)
btn.pack()


root.mainloop()
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("300x300")

txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "Enter text")

e = Entry(root, width=30)
e.pack()
e.insert(0, "Enter 1 line")

def btncmd():
    print(txt.get("1.0", END))
    print(e.get())

    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="click", command=btncmd)
btn.pack()


root.mainloop()
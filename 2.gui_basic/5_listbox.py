from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("300x300")

listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "apple")
listbox.insert(1, "cherry")
listbox.insert(2, "banana")
listbox.insert(END, "melon")
listbox.insert(END, "grape")
listbox.pack()

def btncmd():
    #listbox.delete(END)
    #print(listbox.size())
    #print(listbox.get(0, END))
    #print(listbox.curselection())
    #listbox.delete(listbox.curselection())

btn = Button(root, text="click", command=btncmd)
btn.pack()


root.mainloop()
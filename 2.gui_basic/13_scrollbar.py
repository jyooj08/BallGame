from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("300x300")

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)
for i in range(1, 32): # 1~31
    listbox.insert(END, str(i) + " day")
listbox.pack(side="left")

#listbox와 scrollbar mapping
scrollbar.config(command=listbox.yview)

root.mainloop()
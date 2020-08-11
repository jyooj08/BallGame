from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("300x300")

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="gui_basic/image.png")
photo2 = PhotoImage(file="gui_basic/image2.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="hello")
    label2.config(image=photo2)


btn = Button(root, text="click", command=change)
btn.pack()

root.mainloop()
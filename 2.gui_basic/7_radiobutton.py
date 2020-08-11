from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("300x300")

Label(root, text="select menu").pack()

burger_var=IntVar()
btn_burger1 = Radiobutton(root, text="hamburger", value=1, variable=burger_var)
btn_burger2 = Radiobutton(root, text="cheeseburger", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="chickenburger", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="select drink").pack()
drink_var=StringVar()
btn_drink1 = Radiobutton(root, text="coke", value="coke", variable=drink_var)
btn_drink2 = Radiobutton(root, text="sprite", value="sprite", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()

def btncmd():
    print(burger_var.get())
    print(drink_var.get())

btn = Button(root, text="click", command=btncmd)
btn.pack()


root.mainloop()
from tkinter import *

root = Tk()

e = Entry(root, width = 50)
e.pack()
e.insert(0, "Enter your name: ")


def myClick():
	hello = "Hello: " + e.get()
	myLabel1 = Label(root, text = hello )
	myLabel1.pack()


myButton = Button(root, text = "Coggers", command = myClick)
myButton.pack()

root.mainloop()

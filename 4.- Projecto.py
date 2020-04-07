from tkinter import *

root = Tk()

def myClick():
	myLabel = Label(root,text="Look i clicked a button!!")
	myLabel.pack()


myBottom = Button(root, text = "Apretame", command = myClick)
myBottom.pack()

root.mainloop()

# Command te permite hacer que un boton o algo cumpla una funcion (Def)fg

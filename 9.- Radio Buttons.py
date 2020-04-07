from tkinter import *
from PIL import ImageTk,Image

root = Tk()

#r = IntVar()
#r.set("2")

def click(value):
    my_label = Label(root,text=value)
    my_label.pack()

MODES = [
            ("Kaori Miyazono" , "Kaori Miyazono"),
            ("Asuna" , "Asuna"),
            ("Shiro"  ,"Shiro"),
            ("Zero" , "Zero"),
        ]
anime = StringVar()
anime.set("Kaori Miyazono")

for text, mode in MODES:
    Radiobutton(root,text=text,variable=anime,value=mode,command= lambda:click(anime.get())).pack(anchor=W)

#Radiobutton(root, text="Option 1", variable=r,value=1,command= lambda : click(r.get())).pack()
#Radiobutton(root, text="Option 2", variable=r,value=2,command= lambda : click(r.get())).pack()

#my_label = Label(root,text=anime.get())
#my_label.pack()

myButton = Button(root,text = "Click me ", command= lambda:click(anime.get()))
myButton.pack()

mainloop()

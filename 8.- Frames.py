from tkinter import *
from PIL import ImageTk,Image

root = Tk()

frame = LabelFrame(root,text="This is a frame...",padx=50,pady=50)
frame.pack(padx=10,pady=10)

button_frame = Button(frame,text="asd")
button_frame.grid(row=1,column=1)

button_test = Button(frame,text="asd")
button_test.grid(row=0,column=0)

root.mainloop()

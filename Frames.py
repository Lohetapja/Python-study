from tkinter import *




window = Tk()

frame = Frame(window,bg="blue",bd=5,relief=SUNKEN)
frame.pack(x=100,y=100)  # side=BOTTOM

button = Button(frame,text="W",font=("Consolas",20),width=3).pack(side=TOP)
button = Button(frame,text="A",font=("Consolas",20),width=3).pack(side=LEFT)
button = Button(frame,text="S",font=("Consolas",20),width=3).pack(side=LEFT)
button = Button(frame,text="D",font=("Consolas",20),width=3).pack(side=LEFT)


window.mainloop()
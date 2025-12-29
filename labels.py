from tkinter import *

# widgets = GUI elements: buttons. textbooks. labels. images
# windows = serves as a conteiner to hold or contain these widgets

window = Tk() #instantiate an instance of a window

photo = PhotoImage(file="kwispy.png")

window.geometry("720x720")
window.title("Lohetapja first GUI")
icon = PhotoImage(file="Red_Dragon.png")
window.iconphoto(True,icon)
window.config(background="#1916ab")

label = Label(window,
              text="Hello world",
              font=("Arial",40,"bold"),
              fg="green",
              bg="black",
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound="bottom")
label.pack()
#label.place(x=0,y=0)

window.mainloop() #place window on computer screen
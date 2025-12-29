from tkinter import *

# widgets = GUI elements: buttons. textbooks. labels. images
# windows = serves as a conteiner to hold or contain these widgets

window = Tk() #instantiate an instance of a window
window.geometry("420x420")
window.title("Lohetapja first GUI")
icon = PhotoImage(file="Red_Dragon.png")
window.iconphoto(True,icon)
window.config(background="#5b58f5")

window.mainloop() #place window on computer screen

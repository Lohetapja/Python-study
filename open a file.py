from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\Riivo\\PycharmProjects\\Õppimine2",
                                          title="Open file",
                                          filetypes=(("text files", "*.txt"),
                                          ("all files","*.*")))
    file = open(filepath, "r")
    print(file.read())
    file.close()

window = Tk()
button = Button(window,text="open",command=openFile) # nupp
button.pack()
window.mainloop()

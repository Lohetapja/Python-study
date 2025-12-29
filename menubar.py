from tkinter import *
from tkinter import filedialog


def paste():
    print("Paste")


def copy():
    print("copy")


def cut():
    print("cut")


def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\Riivo\\PycharmProjects\\Õppimine2",
                                    defaultextension=".txt",
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", "*.*"),
                                    ])
    filetext = str(text.get(1.0.END))
    file.write(filetext)
    file.close()
    if file is None:
        return


def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\Riivo\\PycharmProjects\\Õppimine2",
                                          title="Open file",
                                          filetypes=(("text files", "*.txt"),
                                                     ("all files", "*.*")))
    file = open(filepath, "r")
    print(file.read())
    file.close()


window = Tk()

openImage = PhotoImage(file="soon.png")
saveImage = PhotoImage(file="soon.png")
exitImage = PhotoImage(file="soon.png")


menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0, font=("MV Boli", 15))
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=openFile,image=openImage,compound="left")
fileMenu.add_command(label="Save", command=saveFile,image=openImage,compound="left")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit,image=openImage,compound="left")

editMenu = Menu(menubar, tearoff=0, font=("MV Boli", 15))
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=openFile)
editMenu.add_command(label="Copy", command=saveFile)
editMenu.add_command(label="Paste", command=quit)

text = Text(window)
text.pack()

# button = Button(text="save",command=saveFile) # nupp
# button.pack()

# button = Button(window,text="open",command=openFile) # nupp
# button.pack()

window.mainloop()

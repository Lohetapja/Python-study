from tkinter import *
from tkinter import filedialog


def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\Riivo\\PycharmProjects\\Õppimine2",
                                    defaultextension=".txt",
                                    filetypes=[
                                        ("Text file",".txt"),
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
                                          ("all files","*.*")))
    file = open(filepath, "r")
    print(file.read())
    file.close()

window = Tk()
text = Text(window)
text.pack()
button = Button(text="save",command=saveFile) # nupp
button.pack()
button = Button(window,text="open",command=openFile) # nupp
button.pack()
window.mainloop()

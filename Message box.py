from tkinter import *
from tkinter import messagebox # import messagebox from library

def click():
    # while (True): kastike mis ei ähe eest ära
    messagebox.showwarning(title="Warning", message="You have a virus")
    messagebox.showerror(title="error", message="You have a error")
    messagebox.showinfo(title="This is an infor message box", message="You have a message")
    if messagebox.askretrycancel(title="ask ok cancel",message="Do you want to"):
        print("You did it!")
    else:
        print("You canceled a thing")
    if messagebox.askyesno(title="ask yes or no",message="Do you like cake?"):
        print("i like cake too")
    else:
        print("Why dont u like cake?")
    if messagebox.askyesnocancel(title="ask ok cancel",message="Do you want to"):
        print("You did it!")
    else:
        print("You canceled a thing")

    answer = messagebox.askquestion(title="ask question", message="Do you like pie?")
    if(answer == "yes"):
        print("I like cake toooo")
    else:
        print("Why do u not like pie")

    answer = messagebox.askyesnocancel(title="Yes no cancel",message="Do you like to code",icon="warning")
    if(answer==True):
        print("you like to code")
    elif(answer==False):
        print("then why are you watching video about coding")
    else:
        print("You have dodged the question")







window = Tk()

button = Button(window,command=click,text="clikc me")
button.pack()

window.mainloop()
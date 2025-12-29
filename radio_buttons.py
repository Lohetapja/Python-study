from tkinter import *
# widgets = GUI elements: buttons. textbooks. labels. images
# windows = serves as a container to hold or contain these widgets
food = ["pizza", "Hamburger", "hotdog"]


def order():
    if y.get() == 0:
        print("You ordered pizza")
    elif y.get() == 1:
        print("You ordered hamburger")
    elif y.get() == 2:
        print("You orgered hotdog")
    else:
        print("huh")


count = 0


def click():
    global count
    count += 1
    print(count)
# print("Click me!")


def submit():
    username = entry.get()
    print("Hello "+username)
    entry.config(state=DISABLED)


def delete():
    entry.delete(0, END)


def backspace():
    entry.delete(len(entry.get())-1, END)


def display():
    if x.get() == 1:
        print("You agree!")
    else:
        print("You dont agree :(")


window = Tk()                                           # instantiate an instance of a window

pizzaImage = PhotoImage(file="soon.png")
hamburgerImage = PhotoImage(file="soon.png")
hotdogImage = PhotoImage(file="soon.png")
foodImages = [pizzaImage, hamburgerImage, hotdogImage]


y = IntVar()
# photo = PhotoImage(file="")
for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],         # text to radio buttons
                              variable=y,               # groups radiobuttons together if they share same variable
                              value=index,              # assigns each radio button different value
                              padx=20,                # adds padding
                              font=("Impact", 30),
                              image=foodImages[index],       # adds image to radiobutton
                              compound="left",        # adds image and text (left-side)
                              indicatoron=0,          # eliminate circle indicators
                              width=375,
                              command=order             # this will set radiobutton to function
                              )

    radiobutton.config()
    radiobutton.config()
    radiobutton.config()
    radiobutton.pack(anchor=W)

x = IntVar()
button_photo = PhotoImage(file="ScreenHunter.png")
check_button = Checkbutton(window,
                           text="I agree",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=("Arial", 60),
                           fg="Purple",
                           activeforeground="green",
                           activebackground="black",
                           padx=20,
                           pady=10,
                           image=button_photo,
                           compound="left")


check_button.pack()


entry = Entry(window,
              font=("Arial", 20),
              fg="green",
              bg="black",
              show="*")
# entry.insert(0,"Sponge Bob")
entry.pack(side="left")

submit_button = Button(window, text="submit", command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text="delete", command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text="backspace", command=backspace)
backspace_button.pack(side=RIGHT)

button = Button(window,
                text="You want more kwispy? Click me!",
                command=click,
                font=("Comic Sans", 30, ),
                fg="grey",
                bg="black",
                activeforeground="green",
                activebackground="black",
                state=ACTIVE,
                compound="left")
button.pack(anchor=W)

photo = PhotoImage(file="kwispy.png")
window.geometry("1240x1040")
window.title("Lohetapja first GUI")
icon = PhotoImage(file="Red_Dragon.png")
window.iconphoto(True, icon)
window.config(background="#1916ab")

label = Label(window,
              text="Hello world",
              font=("Arial", 40, "bold"),
              fg="green",
              bg="black",
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound="top")
label.pack(),


# label.place(x=0,y=0)

window.mainloop()  # place window on computer screen

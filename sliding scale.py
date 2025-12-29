from tkinter import *

def submit():
    print("The temperature is: "+ str(scale.get())+ " degrees C")

window = Tk()

hotImage = PhotoImage(file="soon.png")
hotLabel = Label(image=hotImage)
hotLabel.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,  #orientation
              font= ("Consolas",10),
              tickinterval= 5,
              showvalue = 0,     #hide current value
              troughcolor= "grey",
              fg = "blue",
              bg= "black"
              )
scale.set(0)        #  alternatiiv  (((scale["from"])-scale["to"]/2)+scale["to"]) 100 ja asemel , current value
scale.pack()

coldImage = PhotoImage(file="soon.png")
coldLabel = Label(image=coldImage)
coldLabel.pack()

button = Button(window,text="submit",command=submit)
button.pack()
window.mainloop()
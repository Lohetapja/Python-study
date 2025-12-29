#**kwargs(KeyWordArguments) = parameter that will pack all arguments into a dictionary
#           useful so that a function can accept a varying amount of keyword arguments

#def hello(first, last):
#    print("Hello " + first + " " + last)
#
#hello(first="Lohe",last="Tapja")

#def hello(**kwargs):
#    print("Hello " + kwargs["first"] + " " + kwargs["last"])
#
#hello(first="Lohe",middle="Code",last="Tapja")


def hello(**kwargs):
#    print("Hello " + kwargs["first"] + " " + kwargs["last"])
    print("Hello",end=" ")
    for key, value in kwargs.items():
        print(value,end=" ")

hello(title="Mr.",first="Lohe",middle="Code",last="Tapja")
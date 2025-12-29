# keyword arguments =   arguments preceded by an identifier when we pass them to a function
#                       the order of the arguments dosen't matter, unlike positional arguments
#                       Python knows the names of the arguments that our function recieves.

def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)

hello(last="Lohe",middle="Tapja",first="Code")    #järjekord ei oma tähtsust, kui just ei määra ise 
# scope =   the region that variable is recognized
#           A variable is available from inside the region it is created
#           A globally and locally scoped versions of a variable  can be created

name = "Tapja" #global scope (available inside and outside functions)

def display_name():
    name = "Lohe" # local scope (available only inside this function)
    print(name)
display_name()
print(name)
                    # L = Local
                    # E = Enclosing
                    # G = Global
                    # B = Built-in
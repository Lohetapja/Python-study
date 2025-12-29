try:
    with open("lab running.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("This file was not found!")

#print(file.closed)
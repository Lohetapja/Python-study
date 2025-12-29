import os

#path = "C:\\Users\\Riivo\\OneDrive\\Desktop\\lab running.txt"  #kui lisada faili asemele kausta nimi saab kontrollida ka kasusta olemasolu

#if os.path.exists(path):
#    print("That location exists!")
#    if os.path.isfile(path):
#        print("That is a file!")
#else:
#    print("That location dose not exist!")


path = "C:\\Users\\Riivo\\OneDrive\\Desktop\\ScreenHunter"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file!")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("That location dose not exist!")
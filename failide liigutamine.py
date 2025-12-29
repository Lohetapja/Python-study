import os

source = "Folder"
destination = "C:\\Users\\Riivo\\OneDrive\\Desktop\\folder"

try:
    if os.path.exists(destination):
        print("There is a file with that name")
    else:
        os.replace(source,destination)
        print(source+ "was moved")
except:
    print(source+ " was not found")
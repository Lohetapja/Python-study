import os
import shutil

path = "folder"  # os.remove("test.txt")  "test.txt"

try:
    # os.remove(path)   #delete a file
    # os.rmdir(path)    #delete a empty dir
    shutil.rmtree(path) #delete a directory containing files
except FileNotFoundError:
    print("This file was not found")
except PermissionError:
    print("You do not have premission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path+ "was deleted")
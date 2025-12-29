# copyfile() =  copies of a content of a file
# copy() =      copyfile() + permission mode + destination can be a directory
# copy2() =     copy() + copyes metadata (file's creation and modification times)k2

import shutil
shutil.copyfile("lab running.txt","copy lab running")   #src (source), dst(destination) , kui lisad peale koma faili aadressi saad copyda faili kuhu tahad peale loomist


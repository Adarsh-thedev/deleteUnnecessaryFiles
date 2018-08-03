import os

folder1Path=(r"")  #Write path of original folder inside the "" after r
folder1Files=os.listdir(folder1Path)

folder2Path=(r"")  #Write path of the folder from which you want files to be deleted inside the "" after r
folder2Files=os.listdir(folder2Path) 

for files in folder1Files:
	if files in folder2Files:
		commonFiles=os.path.join(folder2Path,files)
		os.remove(commonFiles)

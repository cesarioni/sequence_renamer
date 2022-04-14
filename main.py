
import os
from os.path import exists
import tkinter as tk
from tkinter import filedialog, Text

oldPrefix="Ring1B_"
newPrefix="Ring1C_"
fileExtension=".exr"
##path=r"C:\Users\Cesar\Desktop\last class\seqTest"
root=tk.Tk()
path=""
def file_name(prefix,nextNumber,fileExtension, path):
    numDigit = str(nextNumber).rjust(4, '0')
    fileName = prefix + numDigit + fileExtension
    return(os.path.join(path, fileName))
def addFolder():
    folderName=filedialog.askdirectory()
    path=folderName
    print(path)

def renameFiles():
    nextNumber = 0
    while True:
        oldfileName = file_name(oldPrefix, nextNumber, fileExtension, path)
        newfileName = file_name(newPrefix, nextNumber, fileExtension, path)
        if (exists(oldfileName) == False):
            print("no files with that name structure")
            break
        os.rename(oldfileName, newfileName)
        nextNumber += 1


myCanvas=tk.Canvas(root, height=500, width=200, bg="black")
myCanvas.pack()
myFrame=tk.Frame(root, bg="white")
myFrame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
selFolderBtn=tk.Button(root, text="Open file", padx=10, pady=5, fg="white", bg="black", command=addFolder)
selFolderBtn.pack()
renameFilesBtn=tk.Button(root, text="Rename files", padx=10, pady=5, fg="white", bg="black", command=renameFiles )
renameFilesBtn.pack()
root.mainloop()






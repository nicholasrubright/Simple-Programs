import shutil
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title('Git Helper')
root.geometry('350x250')


def main():
    gitpath = 'C:\\Users\\Nicholas\\Documents\\Programming\\@@pragrams'
    projectpaths = 'C:\\Users\\Nicholas\\source\\repos'

    projectFolders = []
    for folderName, subfolders, filenames in os.walk(projectpaths):
        for subfolder in subfolders:
            projectFolders.append(str(subfolder))

    folder = StringVar()
    folderCombobox = ttk.Combobox(root, textvariable = folder)
    folderCombobox.grid(row = 0, column = 0, stick = 'nsew', padx=20, pady=5)
    folderCombobox.config(values = projectFolders)

    copybutton = ttk.Button(root, text = "Copy file")
    copybutton.grid(row = 0, column = 4, padx=10)   

    selectedFolder = str(folder.get())

    readmeValue = IntVar()
    Checkbutton(root, text="Create README", variable = readmeValue).grid(row = 1, column = 0, stick = 'nsew')
    headerValue = IntVar()
    Checkbutton(root, text="Include Header", variable = headerValue).grid(row = 2, column = 0, stick ='nsew')
    
    def copy():
        selectedFolder = str(folder.get())

        for folderName, subfolders, filenames in os.walk(projectpaths):
            for filename in filenames:
                if filename.endswith(".cpp"):
                    if filename == selectedFolder + ".cpp":
                        file = selectedFolder + ".cpp"
                        filepath = os.path.realpath('C:\\Users\\Nicholas\\source\\repos\\' + selectedFolder + '\\' + selectedFolder + '\\' + file)
                        shutil.copy(filepath, gitpath)

                        #os.mkdir(selectedFolder)
                        #shutil.move(selectedFolder, gitpath)
                        #shutil.move(filepath, selectedFolder)
                        
                if headerValue.get() == 1 and filename.endswith(".h") and filename != 'pch.h':
                    headpath = os.path.realpath('C:\\Users\\Nicholas\\source\\repos\\' +  selectedFolder + '\\' + selectedFolder + '\\' + filename)
                    shutil.copy(headpath, gitpath)
        if readmeValue.get() == 1:
            findLoc = open(gitpath + "\\" + "README.md", 'w')
            findLoc.close()
        
    copybutton.config(command = copy)

if __name__ == "__main__":
    main()

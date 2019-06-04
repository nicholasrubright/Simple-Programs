import shutil
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title('Git Helper')
root.geometry('350x250')


def main():
    #   shutil.copy('C:\\Users\\Nicholas\\Desktop\\pre folder\\program.txt', 'C:\\Users\\Nicholas\\Desktop\\post folder')
    gitpath = 'C:\\Users\\Nicholas\\Documents\\Programming\\@@pragrams'
    projectpaths = 'C:\\Users\\Nicholas\\source\\repos'

    projectFolders = []
    for folderName, subfolders, filenames in os.walk(projectpaths):
        for subfolder in subfolders:
            projectFolders.append(str(subfolder))

    folder = StringVar()
    folderCombobox = ttk.Combobox(root, textvariable = folder)
    folderCombobox.grid(row = 0, column = 1, stick = 'nsew', pady = 10, padx = 50)
    folderCombobox.config(values = projectFolders)

    copybutton = ttk.Button(root, text = "Copy file")
    copybutton.grid(row = 0, column = 4, stick = 'nsew', padx = 10, pady = 10)   

    selectedFolder = str(folder.get())
    
    def copy():
        selectedFolder = str(folder.get())

        for folderName, subfolders, filenames in os.walk(projectpaths):
            for filename in filenames:
                if filename.endswith(".cpp"):
                    if filename == selectedFolder + ".cpp":
                        file = selectedFolder + ".cpp"
                        filepath = os.path.realpath('C:\\Users\\Nicholas\\source\\repos\\' + selectedFolder + '\\' + selectedFolder + '\\' + file)
                        shutil.copy(filepath, gitpath)
    
    copybutton.config(command = copy)

if __name__ == "__main__":
    main()

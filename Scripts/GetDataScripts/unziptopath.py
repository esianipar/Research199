import zipfile
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import *

#path_to_zip_file = input("Input path files you wish to extract.\nYou will also be asked to input a directory to extract to.")
Tk().withdraw()
fileName = askopenfilenames(filetypes=[("Tif files", "*.tif"), ("Tif files", "*.tiff"), ("All Files", "*.*")])
directy_to_extract_to = input("Now please input directory to extract to.")

with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
    zip_ref.extractall(directory_to_extract_to)
import os
import tkinter as tk
from tkinter import filedialog


count = 18
def rename_files(path):
    global count  # Add this line to use the global count variable
    files = os.listdir(path)
    
    for file_name in files:
        if os.path.isfile(os.path.join(path, file_name)):
            new_name = count
            new_path = os.path.join(path, str(new_name))  # Convert new_name to string
            os.rename(os.path.join(path, file_name), new_path)
            count += 1
    
    print("File renaming complete!")

def select_path():
    root = tk.Tk()
    root.withdraw()

    path = filedialog.askdirectory(title="Select a directory")

    if path:
        rename_files(path)
    else:
        print("No path selected.")

select_path()

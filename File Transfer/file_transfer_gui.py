#
# Python Ver:   3.9.6
#
# Author:       Jeff Stoppel
#
# Purpose:      To create a UI that will allow the user to browse
#               and choose specific folders. The user will be able
#               to copy files modified in the last 24 hours to a
#               folder of their choice. The user will be able to
#               manually initiate the "file check" process
#
#

import os
import time
import shutil
import tkinter.filedialog as filedialog
import tkinter
from tkinter import *

class ParentWindow(Frame):
    def __init__(self, master):
        Frame. __init__ (self)


    def source():
        source_path = tk.filedialog.askdirectory()
        source_entry.delete(1, tk.END)
        source_entry.insert(0, source_path)


    def destination():
        path = tk.filedialog.askdirectory()
        destination_entry.delete(1, tk.END)
        destination_entry.insert(0, path)


    def copy_files():
        


    top_frame = tk.Frame(master)
    bottom_frame = tk.Frame(master)
    line = tk.Frame(master, height=1, width=400, bg="grey", relief="groove")

    source_path = tk.Label(top_frame, text="Source Folder:")
    source_entry = tk.Entry(top_frame, text="", width=40)
    browse1 = tk.Button(top_frame, text="Browse", command=source)

    destination_path = tk.Label(bottom_frame, text="Folder to receive copies:")
    destination_entry = tk.Entry(bottom_frame, text="", width=40)
    browse2 = tk.Button(bottom_frame, text="Browse", command=destination)

    copy_button = tk.Button(bottom_frame, text="Copy Files", command=copy_files)


    top_frame.pack(side=tk.TOP)
    line.pack(pady=10)
    bottom_frame.pack(side=tk.BOTTOM)

    source_path.pack(pady=5)
    source_entry.pack(pady=5)
    browse1.pack(pady=5)

    destination_path.pack(pady=5)
    destination_entry.pack(pady=5)
    browse2.pack(pady=5)

    copy_button.pack(pady=20, fill=tk.X)






if __name__ == '__main__':
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()

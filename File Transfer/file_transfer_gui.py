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
import tkinter as tk
from tkinter import *




class ParentWindow(Frame):
    def __init__(self, master):
        Frame. __init__ (self)


        # Creating master frame
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(500, 500))
        # Center window function from another file here
        self.master.title('File Transfer')
        self.master.config(bg='lightgray')

        # Creating Frames & line
        top_frame = Frame(self)
        bottom_frame = Frame(self)
        line = Frame(self, height=1, width=500, bg='grey', relief='groove')

        # Packing Frames
        top_frame.pack(side=TOP)
        line.pack(pady=10)
        bottom_frame.pack(side=BOTTOM)

        # Creating Source Folder text field
        self.lblSource = Label(top_frame, text='Source Folder Path:')
        self.txtSource = Entry(top_frame, text='', width=50)















if __name__ == '__main__':
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()

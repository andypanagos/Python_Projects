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
        self.master.geometry('{}x{}'.format(500, 250))
        # Center window function from another file here
        self.master.title('File Transfer')
        

       

        

        # Creating Source Folder text field
        self.lblSource = Label(self.master, text='Source Folder Path:')
        self.lblSource.pack(pady=5)
        self.txtSource = Entry(self.master, text='', width=50)
        self.txtSource.pack(pady=5)
        self.btBrowse = Button(self.master, text='Browse')
        self.btBrowse.pack(pady=5)


        self.line = Canvas(self.master, height=1, width=500, bg='grey', relief='groove')
        self.line.pack(pady=5)
            

        self.lblDestination = Label(self.master, text='Destination Folder Path:')
        self.lblDestination.pack(pady=5)
        self.txtDestination = Entry(self.master, text='', width=50)
        self.txtDestination.pack(pady=5)
        self.btBrowse2 = Button(self.master, text='Browse')
        self.btBrowse2.pack(pady=5)

        
        self.btCopyButton = Button(self.master, text='Copy Files to Destination', width=50)
        self.btCopyButton.pack(pady=5)














if __name__ == '__main__':
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()

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
        center_window(self,500,250)
        self.master.title('File Transfer')

        # Creating Source Folder Label
        self.lblSource = Label(self.master, text='Source Folder Path:')
        self.lblSource.pack(pady=5)
        
        # Source File Path
        self.txtSource = Entry(self.master, text='', width=70)
        self.txtSource.pack(pady=5)
        
        # Browse button
        self.btBrowse = Button(self.master, text='Browse', command=lambda: get_source(self))
        self.btBrowse.pack(pady=5)

        # Line to seperate source section from destination section
        self.line = Canvas(self.master, height=1, width=500, bg='grey', relief='groove')
        self.line.pack(pady=5)
            
        # Creating Destination Folder Label
        self.lblDestination = Label(self.master, text='Destination Folder Path:')
        self.lblDestination.pack(pady=5)
        # Destination File Path
        self.txtDestination = Entry(self.master, text='', width=70)
        self.txtDestination.pack(pady=5)
        # Browse button
        self.btBrowse2 = Button(self.master, text='Browse', command=lambda: destination(self))
        self.btBrowse2.pack(pady=5)

        # Button to copy files from source folder to destination folder
        self.btCopyButton = Button(self.master, text='Copy Files to Destination', width=60, command=lambda: copy_files(self))
        self.btCopyButton.pack(pady=5)



# Defining method to center GUI
def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

# Function to browse and select source folder
def get_source(self):
    self.lblSource = tk.filedialog.askdirectory()
    self.txtSource.delete(0, tk.END)
    self.txtSource.insert(0, self.lblSource)

# Function to browse and select destination folder
def destination(self):
    self.lblDestination = tk.filedialog.askdirectory()
    self.txtDestination.delete(0, tk.END)
    self.txtDestination.insert(0, self.lblDestination)
    

# Method to copy modified files from one folder to another        
def copy_files(self):
    getSource = self.txtSource.get()
    getDestination = self.txtDestination.get()
    source = getSource + '/'                # This adds a '/' to the end of the file path, because the file path inserted into self.txtSource doesn't end with a '/'
    destination = getDestination + '/'      # This adds a '/' to the end of the file path, because the file path inserted into self.txtDestination doesn't end with a '/'
    for fname in os.listdir(source):
        src_fname = os.path.join(source, fname)
        if last_mod_time(src_fname) > before:
            destination_fname = os.path.join(destination, fname)
            shutil.copy(source+fname, destination)
            

# Time Frame
SECONDS_IN_DAY = 24 * 60 * 60
now = time.time()
before = now - SECONDS_IN_DAY

def last_mod_time(fname):
    return os.path.getmtime(fname)









if __name__ == '__main__':
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()

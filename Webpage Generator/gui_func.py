#
# Python Ver:   3.9.6
#
# Author:       Jeff Stoppel
#
# Purpose:      To center the GUI on the user's screen
#
#
#
#


import os
from tkinter import *
import tkinter as tk


import webpage_generator_gui





# This centers the GUI on the user's screen
def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo



if __name__ == '__main__':
    pass

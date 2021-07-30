

import tkinter
from tkinter import *


class ParentWindow(Frame):
    def __init__(self, master):
        Frame. __init__ (self)


        # Creating master frame
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(600, 300))
        self.master.title('Input Text')
        self.master.config(bg='lightgray')


        # Creating text input box
        self.varBodyText = StringVar()

        self.lblBodyText = Label(self.master, text='Enter text: ', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblBodyText.grid(row=0, column=0, padx=(30,0), pady=(30,0))

        self.txtBodyText = Entry(self.master,text=self.varBodyText, font=("Helvetica", 16), fg='black', bg='white')
        self.txtBodyText.grid(row=0, column=1, padx=(30,0), pady=(30,0))
        self.txtBodyText.pack(width=100,height=50)

        # Creating Buttons
        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2)
        self.btnSubmit.grid(row=3, padx=(0,0), pady=(0,0))
        
                             
            
            








if __name__ == '__main__':
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()

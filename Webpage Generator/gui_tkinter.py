

import tkinter
from tkinter import *
import webbrowser

import gui_func



class ParentWindow(Frame):
    def __init__(self, master):
        Frame. __init__ (self)


        # Creating master frame
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(500, 300))
        gui_func.center_window(self,500,300)
        self.master.title('Set Text')
        self.master.config(bg='lightgray')


        # Creating text input box
        self.varBodyText = StringVar()

        self.lblBodyText = Label(self.master, text='Enter text: ', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblBodyText.grid(row=0, column=0, padx=(20,0), pady=(30,0))

        self.txtBodyText = Entry(self.master,text=self.varBodyText, font=("Helvetica", 16), fg='black', bg='white')
        self.txtBodyText.grid(row=0, column=1, padx=(15,0), pady=(30,0))
        

        # Creating Buttons
        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2, padx=(0,0), pady=(15,0))

        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=1, padx=(15,0), pady=(15,0), sticky=W)
        
                             
    # Defining button functions
    def submit(self):
        bt = self.txtBodyText.get()
        f = open('new_webpage.html', 'w')
        
        webbrowser.open_new_tab('new_webpage.html')


    def cancel(self):
        self.master.destroy()
            
            








if __name__ == '__main__':
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()

#
# Python Ver:   3.9.6
#
# Author:       Jeff Stoppel
#
# Purpose:      To create a script that will transfer files
#               
#


import shutil
import os

# Set where the source of teh files are
source = '/Users/jstop/Documents/GitHub/Python_Projects/File Transfer/Folder A/'

# Set the destination path to Folder B
destination = '/Users/jstop/Documents/GitHub/Python_Projects/File Transfer/Folder B/'
files = os.listdir(source)

for i in files:
    # Move files represented by 'i' to their new destination
    shutil.move(source+i, destination)

#
# Python Ver:   3.9.6
#
# Author:       Jeff Stoppel
#
# Purpose:      To create a script that will copy new and
#               edited files within the last 24 hours
#

import shutil
import os
import time


SECONDS_IN_DAY = 24 * 60 * 60

# Time frame 
now = time.time()
before = now - SECONDS_IN_DAY

# Set source of the files
source = '/Users/jstop/Documents/GitHub/Python_Projects/File Transfer/Created Files/'

# Set destination path to 'Copied Files'
destination = '/Users/jstop/Documents/GitHub/Python_Projects/File Transfer/Copied Files/'

def last_mod_time(fname):
    return os.path.getmtime(fname)

for fname in os.listdir(source):
    src_fname = os.path.join(source, fname)
    if last_mod_time(src_fname) > before:
        destination_fname = os.path.join(destination, fname)
        shutil.copy(source+fname, destination)




    

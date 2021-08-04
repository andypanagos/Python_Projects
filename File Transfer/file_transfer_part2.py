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

# Set source of the files
source = '/Users/jstop/Documents/GitHub/Python_Projects/File Transfer/Created Files/'

# Set destination path to 'Copied Files'
destination = '/Users/jstop/Documents/GitHub/Python_Projects/File Transfer/Copied Files/'
files = os.listdir(source)

for i in files:
    modifyDate = datetime.datetime.fromtimestamp(os.path.getmtime(file))
    todaysDate = datetime.datetime.today()
    shutil.copy(source+i, destination)

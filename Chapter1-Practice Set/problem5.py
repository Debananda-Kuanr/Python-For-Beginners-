#Label the program written in problem 4 with comments. 

import os   # Importing the os module to work with operating system functions

# Taking directory path input from the user
path = input("Enter directory path: ")

# Checking whether the entered path actually exists
if os.path.exists(path):

    # Printing a heading message
    print("Contents of the directory:")

    # os.listdir(path) returns a list of files and folders in the directory
    for item in os.listdir(path):

        # Printing each file or folder name
        print(item)

else:
    # This message is shown if the user enters an invalid path
    print("Invalid directory path")

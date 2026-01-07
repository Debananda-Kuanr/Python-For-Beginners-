#Write a python program to print the contents of a directory using the os module. Search online for the function which does that. 

import os

# Specify the directory path
path = input("Enter directory path: ")

# Check if the path exists
if os.path.exists(path):
    print("Contents of the directory:")

    # List and print directory contents
    for item in os.listdir(path):
        print(item)
else:
    print("Invalid directory path")

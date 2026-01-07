#C:\Users\deban\Desktop\Python Course\Chapter1> pip install pyjokes

# https://pyjok.es/  This is a library to get programming jokes


# This is the Single line Comment In Python 


# way1
"""This is the way 
To Print Multiple 
line Comments In
Python"""


# way2
'''This is the way 
To Print Multiple 
line Comments In
Python'''


import pyjokes
# print("Printing a Jokes.....")
joke = pyjokes.get_joke()
print(joke)
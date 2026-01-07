#Install an external module and use it to perform an operation of your interest. 

# Open Terminal and run the following command to install the pyttsx3 module:
# PS C:\Users\deban\Desktop\Python Course> pip install pyttsx3

import pyttsx3
engine = pyttsx3.init()
engine.say("A Warm Good Morning to all of you. Now i am learning text to speech conversion.")
engine.runAndWait()
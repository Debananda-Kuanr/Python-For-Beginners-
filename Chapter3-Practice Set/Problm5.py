#Write a program to format the following letter using escape sequence characters. 
#letter = "Dear Harry, this python course is nice. Thanks!"
 
String =input("Enter your name:")
letter = "Dear %s,\n\tThis python course is nice.\n\tThanks!" %String
print(letter)
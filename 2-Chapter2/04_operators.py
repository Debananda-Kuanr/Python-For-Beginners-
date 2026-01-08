#Arithmetic Operators
print(5+3)  # Addition
print(5-3)  # Subtraction
print(5*3)  # Multiplication
print(5/3)  # Division
print(5%3)  # Modulus (remainder)
print(5**3) # Exponentiation (power)
print(5//3) # Floor Division

#Assignment Operators
x = 5
x += 3  # Equivalent to x = x + 3
x -= 2  # Equivalent to x = x - 2
x *= 4  # Equivalent to x = x * 4
x /= 2  # Equivalent to x = x / 2
print(x)

#Comparison Operators
print(5 == 3)  # Equal to
print(5 != 3)  # Not equal to
print(5 > 3)   # Greater than
print(5 < 3)   # Less than
print(5 >= 3)  # Greater than or equal to
print(5 <= 3)  # Less than or equal to

#Logical Operators
a = True
b = False
print(a and b)  # Logical AND
print(a or b)   # Logical OR
print(not a)     # Logical NOT

#Truth tables for Logical Operators
# AND Operator
print("True AND True =", True and True)#True
print("True AND False =", True and False)#False
print("False AND True =", False and True)#False
print("False AND False =", False and False)#False

# OR Operator
print("True OR True =", True or True)#True
print("True OR False =", True or False)#True
print("False OR True =", False or True)#True
print("False OR False =", False or False)#False

#Not Operator
print("NOT True =", not True)#False
print("NOT False =", not False)#True
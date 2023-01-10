import cmath

# Function to calculate the  cosine of a number
def cosine():
    # Asks the user for input, and then stores it as a variable
    num = float(input("Enter a number: "))
    # Calculates the cosine of the number
    result = cmath.cos(num)
    # Prints the result to the terminal
    print("The result is:" + result)

# Function to calculate the sine of a number
def sine():
    # Asks the user for input, and then stores it as a variable
    num = float("Enter a number: ")
    # Calculates the sine of the input, then stores it as a variable
    result = cmath.sin(num)
    # Prints the result to the terminal
    print("The result is: " + result)
    
# Function to calculate the tangent of a number
def tangent():
    # Asks the user for input, and then stores it in a variable
    num = float("Enter a number: ")
    # Calculates the tangent of the number, then stores it as a variable
    result = cmath.tan(num)
    # Prints the result to the terminal
    print("The result is: " + result)
    
#

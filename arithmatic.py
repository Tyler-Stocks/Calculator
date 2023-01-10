# Import to allow the use of complex numbers
import cmath ; import math

# Function to add two numbers
def addition():
    # Asks the user to input the first number then stores it in a variable
    numOne = float(input("Enter a number: "))
    # Asks the user to input the second number then stores it in a variable
    numTwo = float(input("Enter a second number: "))
    # Adds the two numbers together then stores the result in a variable
    result = numOne + numTwo
    # Prints the result to the terminal
    print("The result is: " + str(result))

# Function to subtract two numbers
def subtraction():
    # Asks the user to input the first number then stores it in a variable
    numOne = float(input("Enter a number: "))
    # Asks the user to input the second number then stores it in a variable
    numTwo = float(input("Enter a second number: "))
    # Adds the two numbers together then stores the result in a variable
    result = numOne - numTwo
    # Returns the result
    print("The result is: " + str(result))
    
# Function to multiply two numbers
def multiplication():
    # Asks the user to input the first number then stores it in a variable
    numOne = float(input("Enter a number: "))
    # Asks the user to input the second number then stores it in a variable
    numTwo = float(input("Enter a second number: "))
    # Adds the two numbers together then stores the result in a variable
    result = numOne * numTwo
    # Prints the result to the terminal
    print("The result is: " + str(result))
    
# Function to divide two numbers
def division():
    # Asks the user to input the first number then stores it in a variable
    numOne = float(input("Enter a number: "))
    # Asks the user to input the second number then stores it in a variable
    numTwo = float(input("Enter a second number: "))
    # Checks to see if the second number is zero
    if numTwo == 0:
        print("Cannot divide by zero")
    else:
        # Adds the two numbers together then stores the result in a variable
        result = numOne / numTwo
    # Returns the result
    print("The result is: " + str(result))

# Function to calculate modulo
def modulo():
    # Asks the user for the first number, and then stores it in a variable
    numOne = int(input("Enter the first number: "))
    # Asks the user for the second number, and then stores it in a variable
    numTwo = int(input("Enter the second number: "))
    # Takes the modulo, and then stores it in a variable
    result = numOne % numTwo
    # Prints the result to the terminal
    print("The result is: " + result)
    
# Function to calculate the square root of a rational number
def squareRoot():
    # Asks the user to input a number, and then stores it as a variable
    num = float(input("Enter a number: "))
    # Takes the square root of the user input, and then stores it as a variable
    result = cmath.sqrt(num)
    # Prints the result to the terminal
    print("The result is: " + result)
    
# Function to calculate the cube root of a number
def cubeRoot():
    # Asks the user to input a number, and then stores it as a variable
    num = float(input("Enter a number: "))
    # Takes the cubed root of the input, and then stores it as a variable
    result = num ** (1/3)
    # Prints the result to the terminal
    print("The result is " + result)

# Function to calculate the log of a number to the specified base
def logarithm():
    # Asks the user to input a number, and then stores it as a variable
    numOne = float(input("Enter the number: "))
    # Asks the user to input the bases, and then stores it as a variable
    numTwo = float(input("Enter the base: "))
    # Takes the log of the number to the specified base, and then turns it into a variable
    result = math.log(numOne, numTwo)
    # Prints the result to the terminal
    print("The result is " + result)

# Function to calculate the factorial of a number
def factorial():
  # Asks the user to input a number, then stores the number in a variable
  num = int(input("Enter a number: "))
  # Initialize the factorial to 1
  factorial = 1
  # Calculate the factorial
  for i in range(2, num+1):
    factorial *= i
  # Prints the result in the terminal
  print(f"The factorial of {num} is {factorial}.")

# Function to add two numbers
def power():
    # Asks the user to input the first number then stores it in a variable
    numOne = float(input("Enter the base: "))
    # Asks the user to input the second number then stores it in a variable
    numTwo = float(input("Enter the exponent: "))
    # Adds the two numbers together then stores the result in a variable
    result = numOne ** numTwo
    # Prints the result to the terminal
    print("The result is: " + str(result))

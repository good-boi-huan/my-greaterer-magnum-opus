# Warm up

# for i in range(1, 6):
#   for j in range(0, i):
#     print(j+1, end="")
#   print()

# number = int(input("Give me a number."))

# if number > 0:
#   print(f"Your number {number} is positive.")
# elif number == 0:
#   print("Your number is 0.")
# else:
#   print(f"Your number {number} is negative.")

# Functions

# Definition: inputs provide a single output
# Programming definition: functions take in inputs (parameters) and return values
# time consuming and inefficient to not use functions
# break up code into chunks and reuse it
# makes code more organized

# Defining a function with no parameters ()
# def HelloWorld():
#   print("Hello World")

# Calling a function
# HelloWorld()

# Function with parameters ()
# def greeting(name):
#   print(f"Hello {name}")

# my_name = input("What is your name? ")
# greeting(my_name)

# Function with no return values = void function

# Return function (returns value)
# Return statements are always the last thing in the function
# def addNumber(inputNumber, inputNumber2):
#   output = int(inputNumber) + int(inputNumber2)
#   return output
# num1 = input("Give me a number ")
# num2 = input("Give me a number ")

# print(addNumber(num1, num2))

# Multiplication Function
# def multiply(input1, input2):
#   output = int(input1) * int(input2)
#   return output

# num1 = input("Give me a number ")
# num2 = input("Give me a number ")
# print(multiply(num1, num2))

# Python packages
# Packages/libraries contain useful functions that we can use
# Ex: random, turtle, example games
# To use a library, call import statement
# Ex: import turtle
# If you don't know the name of the function, look at the documentation

# import turtle
# wn = turtle.Screen()
# z = turtle.Turtle()
# z.speed(1)
# z.forward(100)
# z.left(90)
# z.forward(100)
# z.left(90)
# z.backward(50)

import turtle

z = turtle.Turtle()
z.penup()
z.sety(100)
z.pendown()

sides = int(input("How many sides of a polygon do you want? "))
angle = 360/sides
play = True

while play == True:
  for shape in range(0, sides):
    z.forward(50)
    z.right(angle)
  play_again = input("Do you want to play again (y/n)? ")
  if play_again == "y":
    sides = int(input("How many sides of a polygon do you want? "))
    angle = 360/sides
  else:
    play = False
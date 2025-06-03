# 🌟 Exercise 1 : Hello World
# Instructions
# Print the following output in one line of code:

print("Hello World\n" * 4)

# 🌟 Exercise 2 : Some Math
# Instructions
# Write code that calculates the result of: (99^3)*8 (meaning 99 to the power of 3, times 8).

print((99**3)*8)

# 🌟 Exercise 3 : What is the output ?
# Instructions
# Predict the output of the following code snippets:

# >>> 5 < 3 (FALSE)
# >>> 3 == 3 (TRUE)
# >>> 3 == "3" (FALSE)
# >>> "3" > 3 (FALSE)
# >>> "Hello" == "hello" (FALSE)

# 🌟 Exercise 4 : Your computer brand
# Instructions
# Create a variable called computer_brand which value is the brand name of your computer.
# Using the computer_brand variable print a sentence that states the following: "I have a <computer_brand> computer".

computer_brand = "Asus"
print("I have an", computer_brand, "computer")

# 🌟 Exercise 5 : Your information
# Instructions
# Create a variable called name, and set it’s value to your name.
# Create a variable called age, and set it’s value to your age.
# Create a variable called shoe_size, and set it’s value to your shoe size.
# Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2 and 3.
# Have your code print the info message.
# Run your code

name = "Alex"
age = 29
shoe_size = 42
info = f"My name is {name} and I am {age} years old, and my shoe size is {shoe_size}."

print(info)

# 🌟 Exercise 6 : A & B
# Instructions
# Create two variables, a and b.
# Each variable value should be a number.
# If a is bigger then b, have your code print Hello World.

A = 4
B = 3

if A > B:
    print("Hello world")

# 🌟 Exercise 7 : Odd or Even
# Instructions
# Write code that asks the user for a number and determines whether this number is odd or even.

number = input("Enter number: ")

if int(number) % 8 == 0:
    print("even")

else:
    print("odd")

# 🌟 Exercise 8 : What’s your name ?
# Instructions
# Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome.

name = "Alex"
user_input = input("What is your name? ")

if name != "Alex":
    print("haha, we have the same name!")

else:
    print("That's an odd name!")

# 🌟 Exercise 9 : Tall enough to ride a roller coaster
# Instructions
# Write code that will ask the user for their height in centimeters.
# If they are over 145cm print a message that states they are tall enough to ride.
# If they are not tall enough print a message that says they need to grow some more to ride.

height = int(input("What is your height? "))
if height > 145:
    print("You are tall enough to ride!")
else:
    print("You are too short!")

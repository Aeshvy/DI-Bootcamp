# ✅1. Value Types :

int  # 5, -10	Whole numbers
float  # 3.14, -0.5	Numbers with decimals
str  # "hello"	Strings (text)
bool  # True, False	Boolean value

# ✅2. Variables :

x = 10
name = "Alex"

# 1. Variables are case-sensitive.
# 2. Can be reassigned (x = 20).
# 3. Variable names should be descriptive.

# ✅3. Conditionals :

age = 18

if age >= 18:
    print("Adult")
else:
    print("Minor")


# 🌟Exercise 1 : Strings Are...

description = "strings are..."

# make it all uper case
# replace the word "are" to "is"
# print just the word "strings"

print(description.upper())
print(description.replace("are", "is"))
print(description.replace("are..", " "))

# 🌟Exercise 2 : Your Age
# In the python shell, Create a variable called my_age, use python to know how old you will be in 123879 years:

my_age = (29)
print(my_age + 123879)

# 🌟Exercise 3 : Types of Variables
# Check what is the type of each value, then change it: if it is a string, make it an integer and vice-versa:

bank_balance = '33000'
phone_number = 532287514

print(type(bank_balance))
print(type(phone_number))

print(int(bank_balance))
print(str(phone_number))

# 🌟Exercise 4 : Your Full Name
# In the python shell, Create a variable called first_name and a variable called last_name, and then print your full name using those two variables

fname = "Alex"
lname = "Eshy"
print(fname, lname)

# 🌟Exercise 5 : Boolean Variables
# Given the following values:

x = 5
y = 10
z = 0
word1 = "hello"
word2 = "world"

# 1. Check if x is less than y and y is greater than z.
# 2. Verify if word1 is not equal to word2.
# 3. Use the bool() function to check the boolean value of z and word1.

print(x<y and y>z)
print(word1 != word2)
print(bool(z) , bool(word1))

# 🌟Exercise 6 : f-strings
# You have a friend named Alice, and you want to send her a message with the following details:
# Use f-strings to print a message saying:

"Hello, Alice! You are 30 years old and live in New York."
# Use str.format() to print the same message.

Name = "Alice"
Age = 30
City =  "New York"
print(f"Hello, {Name}! You are {Age} years old and live in {City}.")

# 🌟 Exercise 7 : FizzBuzz
# Ask the user for a number between 1 and 100
# If the number is a multiple of three, print Fizz
# If the number is a multiple of five, print Buzz.
# If the number is a multiple is a multiples of both three and five, print FizzBuzz instead.

number_input = int(input("Enter a number between 1 and 100: "))

if number_input % 15 == 0:
    print("Fizzbuzz")
elif number_input % 5 == 0:
    print("Fizz")
elif number_input % 3 == 0:
    print("Buzz")
else:
    print("No Hablo Espanol")

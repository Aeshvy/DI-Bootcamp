# Password Encryptor



# Password Generator (With Input)

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Python Password Generator!")

num_letters = int(input("How many letters would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))
num_symbols = int(input("How many symbols would you like?\n"))

password = ''

for letter in range(0, num_letters):
    # random_letter = random.choice(letters)
    # password += random_letter
    password += random.choice(letters)

for number in range(0, num_numbers):
    # random_number = random.choice(numbers)
    # password += random_number
    password += random.choice(numbers)

for symbol in range(0, num_symbols):
    # random_symbol = random.choice(symbols)
    # password += random_symbol
    password += random.choice(symbols)

password=''.join(random.sample(password,len(password)))
print(password)


password_list = []

for letter in range(0, num_letters):
    password_list.append(random.choice(letters))

for number in range(0, num_numbers):
    password_list.append(random.choice(numbers))

for symbol in range(0, num_symbols):
    password_list.append(random.choice(symbols))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""

for char in password_list:
    password += char
print(f'Your new password is: {password}')


# Password Generator (Without Input)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Python Password Generator!")
user_input = input('Would you like to generate a password?\nType "Y" for Yes or "N" for No: ').lower()

password = ''

if user_input == 'y':

    for letter in range(0, 5):
        # random_letter = random.choice(letters)
        # password += random_letter
        password += random.choice(letters)

    for number in range(0, 5):
        # random_number = random.choice(numbers)
        # password += random_number
        password += random.choice(numbers)

    for symbol in range(0, 5):
        # random_symbol = random.choice(symbols)
        # password += random_symbol
        password += random.choice(symbols)

    password=''.join(random.sample(password,len(password)))
    print(password)

else:
    user_input == 'n'
    print("Good day to you!")


# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print('FizzBuzz')
#     elif number % 3 == 0:
#         print('Fizz')
#     elif number % 5 == 0:
#         print('Buzz')
#     else:
#         print(number)
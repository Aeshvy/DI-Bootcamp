# 🌟 Exercise 1: Currencies

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

# Using the code above, implement the relevant methods and dunder methods which will output the results below.

    def __str__(self):
        return f"{self.amount} {self.currency}s"

    def __repr__(self):
        return f"{self.amount} {self.currency}s"

    def __int__(self):
        return self.amount

    def __add__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return Currency(self.currency, self.amount + other.amount)
        elif isinstance(other, int):
            return Currency(self.currency, self.amount + other)
        raise TypeError(f"Unsupported addition with type {type(other)}")

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))

print(int(c1))

print(repr(c1))

print(c1 + 5)

print(c1 + c2)

print(c1)

c1 += 5
print(c1)

c1 += c2
print(c1)

# print(c1 + c3)        # When adding 2 currencies which don’t share the same label you should raise an error.

# ---------------------------------------------------------------------------

from func import sum_number

# 🌟 Exercise 2: Import

# In a file named func.py create a function that sum 2 numbers, and prints the result
# In a file named exercise_one.py import the function and call it to print the result

sum_number()

# ---------------------------------------------------------------------------

import string, random

# 🌟 Exercise 3: String module

# Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# Hint: use the string module

random_string = ''.join(random.choice(string.ascii_letters) for i in range(5))
print(random_string)

# ---------------------------------------------------------------------------

from datetime import datetime

# 🌟 Exercise 4 : Current Date

# Create a function that displays the current date.
# Hint : Use the datetime module.

now_date = datetime.now()
print(now_date)

# ---------------------------------------------------------------------------

# 🌟 Exercise 5 : Amount of time left until January 1st

# Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st of January is in 10 days and 10:34:01hours).

def time_until_july(target_date):
    now = datetime.now()

    time_diff = target_date - now

    print(f'The 1st of January is in {time_diff} hours')

target_date = datetime(2026, 1, 1, 23, 59, 59)
time_until_july(target_date)

# ---------------------------------------------------------------------------

# 🌟 Exercise 6 : Birthday and minutes

# Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.

def minutes_lived(birthdate):
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    minutes_lived = (int((datetime.now() - birthdate).total_seconds() / 60))

    print(f'You have lived: {minutes_lived} seconds.')

birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
minutes_lived(birthdate)

# ---------------------------------------------------------------------------

from faker import Faker

# 🌟 Exercise 7 : Faker Module

# Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
# Create an empty list called users. Tip: It should be a list of dictionaries.
# Create a function that adds new dictionaries to the users list. Each user has the following keys: name, adress, langage_code. Use faker to populate them with fake data.

users = []

def add_user():
    fake = Faker()
    user = {
        "name": fake.name(),
        "address": fake.address(),
        "language_code": fake.language_code(),
    }
    users.append(user)

for user in range(3):
    add_user()

for user in users:
    print(user)


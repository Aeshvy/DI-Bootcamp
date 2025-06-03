# 🌟 Exercise 1 : Favorite Numbers
# Instructions
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

my_fav_numbers = {1, 2, 3, 4}
my_fav_numbers.add(5)
my_fav_numbers.add(6)

my_fav_numbers.remove(6)

print(my_fav_numbers)

friend_fav_numbers = {10, 11, 12, 13, 14, 15}

our_fav_numbers = my_fav_numbers | friend_fav_numbers

print(our_fav_numbers)

# 🌟 Exercise 2: Tuple
# Instructions
# Given a tuple which value is integers, is it possible to add more integers to the tuple?

# No, Tuples are immutable lists, which means items can’t be changed.


# 🌟 Exercise 3: List
# Instructions
# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.pop(0)
basket.pop(-1)
basket.append("Kiwi")
basket.insert(0, "Apples")

sum = basket.count("Apples")
basket.clear()

print(basket)

# 🌟 Exercise 4: Floats
# Instructions
# Recap – What is a float? What is the difference between an integer and a float?
# Create a list containing the following sequence of floats and integers (it should be a list with mixed types): 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
# Can you think of another way to generate a sequence of floats?

list = []

for i in range(1, 5):
    list.append(i + 0.5)
    list.append(i)

print(list)

sequence = [1, 2, 3, 4, 5]
sequence.insert(0, 0.5)
sequence.insert(2, 1.5)
sequence.insert(4, 2.5)
sequence.insert(6, 3.5)

print(sequence)

# 🌟 Exercise 5: For Loop
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

for number in range(1, 21):
    print(number)

for number in range(1, 21):
    if number % 2 == 0:
        print(number)

# 🌟 Exercise 6 : While Loop
# Instructions
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.

name = " "

while name != "Alex":
    name = input("What is your name? ")
    if name != "Alex":
        print("WRONG!")
else:
    print("Congratulations!")

# 🌟 Exercise 7: Favorite fruits
# Instructions
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

favorite_fruit = input("Pick your favorite fruits, separated by spaces: ")
favorite_fruit_list = favorite_fruit.split()
print(favorite_fruit_list)

fruit_choice = input("pick one favorite fruit: ")
if fruit_choice in favorite_fruit_list:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit!")

# 🌟 Exercise 8: Who ordered a pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

toppings = []
print("Welcome, pleaese add your toppings, and when finished, type 'quit'")

while True:
    topping = input()
    if topping.lower() == 'quit':
        break

    toppings.append(topping)
    print(f"{topping} is added to your order, anything else? ")

total_price = 10 + 2.5 * len(toppings)

print("Your toppings are:")
for topping in toppings:
    print(topping)

print(f"your total price is {total_price}$")

# 🌟 Exercise 9: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Ask a family the age of each person who wants a ticket.

# Store the total cost of all the family’s tickets and print it out.

total_cost = 0
family_members = int(input("Welcome, how many tickets? "))

for n in range(1, family_members + 1):

    age = int(input(f"What is the age of member {n}? "))

    if age < 3:
        price = 0
        print(f"Family member {n} ticket is free!")
    elif 3 <= age <= 12:
        price = 10
        print(f"Family member {n} ticket is {price}.")
    else:
        price = 15
        print(f"Family member {n} ticket is {price}.")

    total_cost += price

print(f"The total cost for all tickets is ${total_cost}.")

# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.

teens = ["Alex", "Jenny", "Bob", "Alice"]

for teen in teens:
    age = int(input("What is your age? "))

    if 16 <= age <= 21:
        print(f"{teen} is not allowed to watch the movie.")
        teens.remove(teen)

    elif print(f"{teen} can enter"):
        break

print(f"Teenagers allowed to watch the movie {teens}")

# 🌟 Exercise 10 : Sandwich Orders
# Instructions
# Using the list below :

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich",
                   "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

# The deli has run out of pastrami, use a while loop to remove all occurrences of “Pastrami sandwich” from sandwich_orders.
# We need to prepare the orders of the clients:
# Create an empty list called finished_sandwiches.
# One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

    finished_sandwiches = []

while sandwich_orders:                        # loop for sandwich list
    sandwich = sandwich_orders.pop(0)         # sandwich = updated sandwich list with .pop(0) - first sandwich removed
    finished_sandwiches.append(sandwich)      # finished sandwich list is updated with .append(sandiwch)
    print(f"I made your {sandwich.lower()}")

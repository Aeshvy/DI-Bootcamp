# 🌟 Exercise 1 : Favorite Numbers
# Instructions
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

# ANSWER

# my_fav_numbers = {1, 2, 3, 4}
# my_fav_numbers.add(5); my_fav_numbers.add(6)

# my_fav_numbers.remove(6)

# print(my_fav_numbers)

# friend_fav_numbers = {10, 11, 12, 13, 14, 15}

# our_fav_numbers = my_fav_numbers | friend_fav_numbers

# print(our_fav_numbers)



# 🌟 Exercise 2: Tuple
# Instructions
# Given a tuple which value is integers, is it possible to add more integers to the tuple?

# ANSWER

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

# ANSWER

# basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# # basket.remove(0) - remove(0) is invalid because (0) is not an element in basket !!!
# basket.pop(0); basket.pop(-1)
# basket.append("Kiwi")
# basket.insert(0, "Apples")

# sum = basket.count("Apples")

# print(basket)
# print(sum)

# basket.clear()

# print(basket)



# 🌟 Exercise 4: Floats
# Instructions
# Recap – What is a float? What is the difference between an integer and a float?
# Create a list containing the following sequence of floats and integers (it should be a list with mixed types): 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
# Can you think of another way to generate a sequence of floats?

# ANSWER

# list = []

# for i in range(1, 5):
#     list.append(i + 0.5)
#     list.append(i)

# print(list)

# sequence = [1, 2, 3, 4, 5]
# sequence.insert(0, 0.5); sequence.insert(2, 1.5); sequence.insert(4, 2.5); sequence.insert(6, 3.5)

# print(sequence)



# 🌟 Exercise 5: For Loop
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

# ANSWER


# for number in range(1, 21):
#     print(number)

# for number in range(1, 21):
#     if number % 2 ==0:
#         print(number)




# 🌟 Exercise 6 : While Loop
# Instructions
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.

# ANSWER

# name = " "

# while name != "Alex":
#     name = input("What is your name? ")
#     if name != "Alex":
#         print("WRONG!")
# else:
#     print("Congratulations!")




# 🌟 Exercise 7: Favorite fruits
# Instructions
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

# ANSWER

# favorite_fruit = input("Pick your favorite fruits, separated by spaces: ")
# favorite_fruit_list = favorite_fruit.split()
# print(favorite_fruit_list)

# fruit_choice = input("pick one favorite fruit: ")
# if fruit_choice in favorite_fruit_list:
#     print("You chose one of your favorite fruits! Enjoy!")
# else:
#     print("You chose a new fruit!")

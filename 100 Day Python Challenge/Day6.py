import random

# 1. Randomly choose word from word_list, assign to a variable, and print.
# 2. Ask the user to guess a letter, and assign to variablue (lowercase).
# 3. Check if 'guess' letter is in one of the letters of 'chosen_word'
#   print "Right" if it is.

word_list = ['dragon', 'cat', 'banana', 'apple', 'avatar', 'camel', 'aaalcor']
chosen_word = ""


chosen_word = random.choice(word_list)
print(chosen_word)



placeholder = ""

word_length = len(chosen_word)

for position in range(word_length):
    placeholder += '_'
print(placeholder)

guess = input("Guess a letter: ").lower()

display = ""

for letter in chosen_word:
    if guess == letter:
        display += letter
    else:
        display += '_'
print(display)






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
    placeholder += "_"
print(placeholder)


game_over = False
correct_letters = []

while not game_over:
    display = ""
    guess = input("Guess a letter: ").lower()

    for letter in chosen_word:
        if letter == guess:
            display += letter
        else:
            display += "_"
            
    for letter in display:
        display += correct_letters
        print(correct_letters)
    
    print(display)

    if "_" not in display:
        game_over = True
        print("You win!")
    
    
    








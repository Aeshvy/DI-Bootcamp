# 🌟Challenge 1
# Ask a user for a word
# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.

# Make sure the letters are the keys.
# Make sure the letters are strings.
# Make sure the indexes are stored in a list and those lists are values.

word = input('pick a word: ')

dictionary = {}
# iterate through characters of string 'word'
for index, letter in enumerate(word):
    # This checks if the character (letter) is already a key in the dictionary
    if letter in dictionary:
        # If character (letter) is a key in the dictionary, move to next step
        dictionary[letter].append(index)
    # This line is executed when the letter is not found in the dictionary. It creates a new key-value pair in {dictionary}
    else:
        dictionary[letter] = [index]

print(dictionary)

# 🌟Challenge 2
# Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
# Sort the list in alphabetical order.
# Return “Nothing” if you can’t afford anything from the store.

wallet = int(input('What is your budget? '))


def affordable_items():

    items_purchase = {
        "Phone": "$999",
        "Speakers": "$300",
        "Laptop": "$5,000",
        "PC": "$1200"
    }

    affordable = []

    # Checks each item in the store and see if the user can afford it
    for item, price in items_purchase.items():

        # Convert the price by replacing '$' with ',' from dictionary price
        item_price = float(price.replace('$', '').replace(',', ''))

        # If User can afford the item, .append (add) to the affordable list
        if wallet >= item_price:
            affordable.append(item)

    # Sort the affordable items alphabetically
    affordable.sort()

    if affordable:
        # Print the result (affordable), otherwise, print "Nothing"
        print("Items you can afford:", ', '.join(affordable))
    else:
        print("Nothing")


# Calls the function to run the program
affordable_items()

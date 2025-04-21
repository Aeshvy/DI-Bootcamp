# 🌟 Challenge 1 : Sorting

# Instructions
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Use List Comprehension


# Example:

# Suppose the following input is supplied to the program: without,hello,bag,world
# Then, the output should be: bag,hello,without,world

user_input = input("Enter a comma-separated sequence of words: ")

sorted_sequence = ','.join([word.strip() for word in sorted(user_input.split(','))])

print("Sorted sequence:", sorted_sequence)

# ---------------------------------------------------------------------------

# 🌟 Challenge 2 : Longest Word

# Write a function that finds the longest word in a sentence. If two or more words are found, return the first longest word.
# Characters such as apostrophe, comma, period count as part of the word (e.g. O’Connor is 8 characters long).

# Examples:

# longest_word("Margaret's toy is a pretty doll.") ➞ "Margaret's"
# longest_word("A thing of beauty is a joy forever.") ➞ "forever."
# longest_word("Forgetfulness is by all means powerless!") ➞ "Forgetfulness"


def find_longest_word(sentence):
    words = [word for word in sentence.split()]
    return max(words, key=len)

sentence = input("Enter a sentence: ")
longest_word = find_longest_word(sentence)
print(longest_word)
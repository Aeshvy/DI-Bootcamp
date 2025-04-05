# Daily challenge : Text Analysis

import string
from collections import Counter

# The goal of the exercise is to create a class that will help you analyze a specific text. A text can be just a simple string, like “Today, is a happy day” or it can be an external text file.

# Part I
# First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”

# Create a class called Text that takes a string as an argument and store the text in a attribute.
# Hint: You need to manually copy-paste the text, straight into the code

class Text:
    def __init__(self, string):
        self.string = string

    def most_frequent(self, word):
        words = self.string.lwoer().split()
        return words.count(word.lower())

    def most_common(self):
        words = self.string.lower().split()
        if not words:
            return None
        frequent = {}
        for word in words:
            frequent[word] = frequent.get(word, 0) + 1
        return max(frequent, key=frequent.get)

    def most_unique(self):
        wordlist = self.string.lower().split()
        word_count = {}
        for word in wordlist:
            word_count[word] = word_count.get(word, 0) + 1
        unique_words = [word for word, count in word_count.items() if count == 1]
        return unique_words
    
    @classmethod
    def from_file(cls, filename):
        try:
            with open(filename, "r") as file:
                content = file.read()
            return cls(content)
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        return None

text = Text.from_file('the_stranger.txt')

# print(text.most_frequent())
print(text.most_common())
print(text.most_unique())
# Daily challenge Text Analysis:

from collections import Counter

# The goal of the exercise is to create a class that will help you analyze a specific text. A text can be just a simple string, like “Today, is a happy day” or it can be an external text file.

# Part I
# First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”

# Create a class called Text that takes a string as an argument and store the text in a attribute.
# Hint: You need to manually copy-paste the text, straight into the code

class Text:
    def __init__(self, text):
        self.text = text

    def most_frequent(self, word):
        words = self.text.lower().split()
        count = words.count(word)
        if count == 0:
            return f"The word '{word}' was not found in the text."
        return count

    def most_common(self):
        words = self.text.lower().split()
        if not words:
            return "The text is empty."
        return Counter(words).most_common(1)[0]

    def most_unique(self):
        return list(set(self.text.split()))
    
    @classmethod
    def from_file(cls, filename: str):
        with open(filename, 'r') as file:
            text = file.read()
        return cls(text)


sample_text = Text("Good book would sometimes cost as much as a good house.")
print(sample_text.most_frequent("good"))
print(sample_text.most_common())
print(sample_text.most_unique())

text = Text.from_file('the_stranger.txt')
print(text.most_frequent('good'))
print(text.most_common())
print(text.most_unique())
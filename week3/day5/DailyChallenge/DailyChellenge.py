# Daily challenge : Text Analysis

# The goal of the exercise is to create a class that will help you analyze a specific text. A text can be just a simple string, like “Today, is a happy day” or it can be an external text file.

# Part I
# First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”

# Create a class called Text that takes a string as an argument and store the text in a attribute.
# Hint: You need to manually copy-paste the text, straight into the code

class Text:
    def __init__(self, text):
        self.text = text

    def most_frequent(self, word):
        words = self.text.lwoer().split()
        words = [w.strip('.,!?;:"()') for w in words]
        return words.count(word.lower())

    def most_common(self):
       words = self.text.lower().split()
        word_frequency = {}
        for word in words:
            word_frequency[word] = word_frequency.get(word, 0) + 1
        
        # Find the word with the highest frequency
        most_common = max(word_frequency, key=word_frequency.get)
        return most_common

    def most_unique(self):
        words = self.text.lower().split()
        unique_words = set(words)
        return list(unique_words)
    
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

sample_text = Text("A good book would sometimes cost as much as a good house.")

# print(text.most_frequent())
print(text.most_common())
# print(text.most_unique())
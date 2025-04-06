class AnagramChecker:

# Create a new file called anagram_checker.py which contains a class called AnagramChecker.

# The class should have the following methods:
# __init__ - should load the word list file (text file) into a variable, so that it can be searched later on in the code.
# is_valid_word(word) – should check if the given word (ie. the word of the user) is a valid word.


    def __init__(self, wordlist_file):
        self.wordlist = self.load_wordlist(wordlist_file)

    def load_wordlist(self, wordlist_file):
        try:
            with open(wordlist_file, 'r') as file:
                return set(word.strip().upper() for word in file.readlines())
        except FileNotFoundError:
            return set()
    
    def is_valid_word(self, word):
        return word.upper() in self.wordlist
    
    def is_anagram(self, word1, word2):
        w1, w2 = word1.upper(), word2.upper()
        return sorted(w1) == sorted(w2) and w1 != w2
    
    def get_anagrams(self, word):
        word = word.upper()
        return [w for w in self.wordlist if self.is_anagram(word, w)]

anagram_checker = AnagramChecker('sowpods.txt')
print(anagram_checker.get_anagrams("table"))
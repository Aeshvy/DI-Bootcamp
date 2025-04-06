class AnagramChecker:
    def __init__(self, wordlist_file):
        self.wordlist = self.load_wordlist(wordlist_file)

    def load_wordlist(self, wordlist_file):
        try:
            with open(wordlist_file, 'r') as file:
                # Read all lines and strip whitespace
                return set(word.strip().upper() for word in file.readlines())
        except FileNotFoundError:
            print(f"Error: The file {wordlist_file} was not found.")
            return set()
    
    def is_valid_word(self, word):
        if word.upper() in self.wordlist:
            print(f"'{word}' is a valid word!")
            return True
        else:
            print(f"'{word}' is not a valid word.")
            return False


anagram_checker = AnagramChecker('sowpods.txt')
anagram_checker.is_valid_word("example")
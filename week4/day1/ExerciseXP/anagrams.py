from anagram_checker import AnagramChecker


def is_valid_word_input(word):
    word = word.strip()
    if not word.isalpha() or ' ' in word:
        print("Error: Enter only one word with alphabetic characters.")
        return None
    return word

def find_anagrams(word, wordlist):
    word = word.upper()
    return [w for w in wordlist if sorted(w) == sorted(word) and w != word]

def main():
    checker = AnagramChecker('sowpods.txt')

    while True:
        print("\n--- ANAGRAM CHECKER ---")
        print("1. Input a word\n2. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '2':
            print("Goodbye!")
            break
        elif choice == '1':
            raw_input = input("Enter a word: ").strip()
            if raw_input.lower() == 'exit':
                print("Goodbye!")
                break

            word = is_valid_word_input(raw_input)
            if not word:
                continue

            is_valid = checker.is_valid_word(word)
            anagrams = find_anagrams(word, checker.wordlist)

            print(f"\nYOUR WORD: {word.upper()}")
            print("This is a valid English word." if is_valid else "This is not a valid English word.")
            print("Anagrams for your word:", ', '.join(anagrams) if anagrams else "No anagrams found.")
        else:
            print("Invalid choice. Please choose 1 or 2.")

if __name__ == '__main__':
    main()


# 🌟 Exercise 1 – Random Sentence Generator
import random

def get_words_from_file(filename):
    with open(filename, 'r') as file:
        return file.read().splitlines()

def get_random_sentence(length, words):
    return ' '.join(random.sample(words, length))

def main():
    print("This program generates a random sentence from a word list.")
    
    try:
        length = int(input("How many words do you want the sentence to have (between 2 and 20)? "))
        
        if 2 <= length <= 20:
            words = get_words_from_file("sowpods.txt")
            print(get_random_sentence(length, words))
        else:
            print("Error: The number must be between 2 and 20.")
    
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
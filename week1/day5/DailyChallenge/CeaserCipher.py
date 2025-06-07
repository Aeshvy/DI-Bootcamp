# " zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba"
alphabet = " abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
get_letter, keyword = 0, []

text = str(input("Enter the text: ")).strip().lower()
key = int(input("Enter the key: "))

if 0 < key <= 26:
    for letter in text:
        get_letter = alphabet.index(letter) + key
        keyword.append(alphabet[get_letter])
    print(" ".join(keyword))
else:
    print("Key must be between 1 and 26!")

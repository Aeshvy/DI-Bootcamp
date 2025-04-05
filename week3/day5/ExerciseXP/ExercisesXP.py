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
        length = int(input("How many words do you want (between 2 and 20)? "))
        
        if 2 <= length <= 20:
            words = get_words_from_file("sowpods.txt")
            print(get_random_sentence(length, words))
        else:
            print("Error: The number must be between 2 and 20.")
    
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")

# if __name__ == "__main__":
#     main()



# 🌟 Exercise 2: Working with JSON

import json


sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Access the nested “salary” key from the JSON-string above.
data = json.loads(sampleJson)
salary = data["company"]["employee"]["payable"]["salary"]

print(salary)

# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
data["company"]["employee"]["birth_date"] = "1995"

new_sampleJson = json.dumps(data)
print(new_sampleJson)

# Save the dictionary as JSON to a file.
with open("employee_data.json", "w") as file:
    json.dump(data, file)

# 🌟 Exercise 1 : What are you learning ?

# Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# Call the function, and make sure the message displays correctly.

def display_message(name='Alex', learning='functions'):
    print(f"I'm {name}, and I am currently learning about {learning}.")

display_message()

# ---------------------------------------------------------------------------

# 🌟 Exercise 2: What’s your favorite book ?

# Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as "One of my favorite books is <title>".
# For example: “One of my favorite books is Alice in Wonderland”
# Call the function, make sure to include a book title as an argument when calling the function.  

def favorite_book(title):
    print(f"One of my favorite books is {title}.")

favorite_book("Atomic Habbits")

# ---------------------------------------------------------------------------

# 🌟 Exercise 3 : Some Geography

# Write a function called describe_city() that accepts the name of a city and its country as parameters.
# The function should print a simple sentence, such as "<city> is in <country>".
# For example “Reykjavik is in Iceland”
# Give the country parameter a default value.
# Call your function.

def describe_city(cityName, countryName='United States'):
    print(f"{cityName} is in {countryName}")

describe_city('Netanya','Israel')

# ---------------------------------------------------------------------------

# 🌟 Exercise 4 : Random

# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100. Use the random module.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.

import random

def number(num):
    if 1 >= num >=100:
        print("Pick number between 1 and 100.")

    random_num = random.randrange(1,100)

    if num == random_num:
        print("It's a match!")
    else:
        print(f"Your number was: {num}, and the winning number is: {random_num}. Better luck next time!")

user_num = int(input('Pick a number between 1 and 100: '))
number(user_num)

# ---------------------------------------------------------------------------

# 🌟 Exercise 5 : Let’s create some personalized shirts !

# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
# Call the function make_shirt().

# Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
# Call the function, in order to make a large shirt with the default message
# Make medium shirt with the default message
# Make a shirt of any size with a different message.

# Bonus: Call the function make_shirt() using keyword arguments.

def make_shirt(size='large', text='I love Python'):
    print(f'The size of the shirt is {size}, and the text is: "{text}."')


def make_shirts(size, text='I love Python'):
    if size == 'large':
        print(f'The size is large, and the text is: "{text}."')
    if size == 'medium':
        print(f'The size is medium, and the text is: "{text}."')
    if size == 'small':
        print(f'The size is small, and the text is: "{text}."')


make_shirts('medium'), make_shirt(size='large', text='Hello World!')

# ---------------------------------------------------------------------------

# 🌟 Exercise 6 : Magicians

# Using this list of magician’s names

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# Create a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the original list of magicians by adding the phrase "the Great" to each magician’s name.
# Call the function make_great().
# Call the function show_magicians() to see that the list has actually been modified.

def show_magician():
    for magician in magician_names:
        print(magician)

def make_great():
    for magician in magician_names:
        print(magician + " the Great")

show_magician()
make_great()

# ---------------------------------------------------------------------------

# 🌟 Exercise 7 : Temperature Advice

# Create a function called get_random_temp().
# This function should return an integer between -10 and 40 degrees (Celsius), selected at random.

def get_random_temp(season):
    if season == 'winter':
        low_limit, high_limit = -10, 16
    elif season == 'autumn':
        low_limit, high_limit = 17, 23
    elif season == 'spring':
        low_limit, high_limit = 24, 32
    elif season == 'summer':
        low_limit, high_limit = 33, 40

    return random.randint(low_limit, high_limit)
    

# Create a function called main().
# Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
# Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”

# Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
# below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
# between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
# between 16 and 23
# between 24 and 32
# between 32 and 40

def main():
    
    season = input('Input a season: ').lower()
    

    temperature = get_random_temp(season)
    print(f'The temperature right now is {temperature} degrees Celsius.')


    if temperature <= 0:
        print("Brrr, that's freezing! Wear some extra layers today")
    elif temperature <= 16:
        print("Quite chilly! Don't forget your coat")
    elif 16 < temperature <= 23:
        print("The weather seems nice")
    elif 24 <= temperature <=32:
        print("Getting quite hot. Maybe wear something short")
    elif 32 < temperature <= 40:
        print("It's getting out of control. Get some sunscreen")
    else:
        print("This is too much. Stay home.")


main()


# Change the get_random_temp() function:
# Add a parameter to the function, named ‘season’.
# Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
# Now that we’ve changed get_random_temp(), let’s change the main() function:
# Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
# Use the season as an argument when calling get_random_temp().

# ---------------------------------------------------------------------------

# 🌟 Exercise 8 : Star Wars Quiz

# This project allows users to take a quiz to test their Star Wars knowledge.
# The number of correct/incorrect answers are tracked and the user receives different messages depending on how well they did on the quiz.

# Here is an array of dictionaries, containing those questions and answers:


data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]


def quiz(data):

    correct_answers = 0
    wrong_answers = []

    for item in data:

        user_answer = input(item["question"] + " ")

        if user_answer.lower() == item["answer"].lower():
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Wrong! The correct answer is: {item['answer']}")
            wrong_answers.append((item["question"], user_answer, item["answer"]))

        print(f"You got {correct_answers} questions out of {len(data)} correct!")
    
    # display_results(correct_answers, len(data) - correct_answers)

    # if wrong_answers:
    #     print("\nHere are the wrong answers:")
    # for question, user_answer, correct_answer in wrong_answers:
    #     print(f"Question: {question}\nYour Answer: {user_answer}\nCorrect Answer: {correct_answer}\n")

      
# def display_results(correct_answers, incorrect_answers):
#     print(f"You got {correct_answers} correct and {incorrect_answers} incorrect answers.\nThank you for playing.")

quiz(data)
  

# Create a function that asks the questions to the user, and check his answers. Track the number of correct, incorrect answers. Create a list of wrong_answers
# Create a function that informs the user of his number of correct/incorrect answers.

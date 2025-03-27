# 🌟 Exercise 1: Cats

# Using this class

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Instantiate three Cat objects using the code provided above.
cat1 = Cat('Peter', 41)
cat2 = Cat('Joe', 46)
cat3 = Cat('Quagmire', 38)

# Outside of the class, create a function that finds the oldest cat and returns the cat.
def find_oldest_cat(cats):
    return max(cats, key=lambda cat: cat.age)

cats = [cat1, cat2, cat3]

oldest_cat = find_oldest_cat(cats)

# Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.
print(f"The oldest is {oldest_cat.name}, he is {oldest_cat.age} years old. Damn, that's like really old!")

# ---------------------------------------------------------------------------

# 🌟 Exercise 2 : Dogs

# Create a class called Dog.
# In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        pass

# Create a method called bark that prints the following string “<dog_name> goes woof!”.
    def bark(self):
        return(f'{self.name} goes woof!')

# Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
    def jump(self):
        h = self.height * 2
        return(f'{self.name} jumps {h} cm high!')

# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
davids_dog = Dog('Rex', 50)

# Print the details of his dog (ie. name and height) and call the methods bark and jump.
print(davids_dog.bark())
print(davids_dog.jump())

# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
sarahs_dog = Dog('Teacup', 20)

# Print the details of her dog (ie. name and height) and call the methods bark and jump.
print(sarahs_dog.bark())
print(sarahs_dog.jump())

# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.
if davids_dog.height > sarahs_dog.height:
    print(f"The bigger dog is {davids_dog.name}.")
else:
    print(f"The bigger dog is {sarahs_dog.name}.")

# ---------------------------------------------------------------------------

# 🌟 Exercise 3 : Who’s the song producer?

# 1. Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

# 2. Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway = Song(["There\’s a lady who\'s sure", 
                 "all that glitters is gold", 
                 "and she\’s buying a stairway to heaven"])

stairway.sing_me_a_song()


# 🌟 Exercise 1 : Pets

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# all_cats = [Bengal, Chartreux, Siamese]

bengal = Bengal("Rob", 3)
chartreux = Chartreux("Bob", 4)
siamese = Siamese("Knob", 5)

all_cats = [bengal, chartreux, siamese]

sara_pets = Pets(all_cats)

sara_pets.walk()


    
# Create another cat breed named Siamese which inherits from the Cat class.
# Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.
# Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the Pet class, and pass the variable all_cats to the new instance.
# Take all the cats for a walk, use the walk method.

# ---------------------------------------------------------------------------

# 🌟 Exercise 2 : Dogs

# Create a class called Dog with the following attributes name, age, weight.
# Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”.
# run_speed: returns the dogs running speed (weight/age*10).
# fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.

# Create 3 dogs and run them through your class.

class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking'

    def run_speed(self):
        return (self.weight / self.age) * 10

    def fight(self, other_dog):
        self_score = self.run_speed() * self.weight
        other_dog_score = other_dog.run_speed() * other_dog.weight

        if self_score > other_dog_score:
            return f"{self.name} wins the fight!"
        elif self_score < other_dog_score:
            return f"{other_dog.name} wins the fight!"

dog1 = Dog("Max", 3, 20)
dog2 = Dog("Lax", 2, 25)
dog3 = Dog("Dax", 4, 18)

# print(dog1.bark())
# print(dog2.bark())
# print(dog3.bark())

# print(f"Max's run speed is {dog1.run_speed():.2f}")
# print(f"Lax's run speed is {dog2.run_speed():.2f}")
# print(f"Dax's run speed is {dog3.run_speed():.2f}")

# print(dog1.fight(dog2))
# print(dog1.fight(dog3))
# print(dog3.fight(dog2))

# ---------------------------------------------------------------------------

# 🌟 Exercise 3 : Dogs Domesticated

# Create a new python file and import your Dog class from the previous exercise.
# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True

# play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.

# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.



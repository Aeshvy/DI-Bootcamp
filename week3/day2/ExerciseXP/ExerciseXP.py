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

print(dog1.bark())
print(dog2.bark())
print(dog3.bark())

print(f"Max's run speed is {dog1.run_speed():.2f}")
print(f"Lax's run speed is {dog2.run_speed():.2f}")
print(f"Dax's run speed is {dog3.run_speed():.2f}")

print(dog1.fight(dog2))
print(dog1.fight(dog3))
print(dog3.fight(dog2))

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


# ****      ANSWER IN IMPORT.PY     ****


# ---------------------------------------------------------------------------

# 🌟 Exercise 4 : Family

# Create a class called Family and implement the following attributes:

# members: list of dictionaries
# last_name : (string)

# Implement the following methods:

# born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.

# is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.

# family_presentation: a method that prints the family’s last name and all the members’ details.

# Create an instance of the Family class, with the last name of your choice, and the below members. Then call all the methods you created in Point 2.


class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, **kwargs):
        kwargs['is_child'] = True
        self.members.append(kwargs)
        print(f"Congratulations! {kwargs['name']} has been born into the family!")

    def is_18(self, name):
        for m in self.members:
            if m.get('name') == name:
                age = m.get('age')
                if age >= 18:
                    print(f"{name} is older than 18.")
                else:
                    print(f"{name} is not older than 18.")
                return age >= 18
        return False

    def family_presentation(self):
        print(f"The {self.last_name} family members:")
        for m in self.members:
            print(f"Name: {m['name']}, Age: {m.get('age', 'Unknown')}, Is Child: {m['is_child']}")

my_family = Family('Eshy')


my_family.members.append({'name':'Michael', 'age':35, 'gender':'Male', 'is_child':False})
my_family.members.append({'name':'Sarah', 'age':32, 'gender':'Female', 'is_child':False})

my_family.born(name='Alex', age=0, gender='Male')

my_family.is_18("Michael")
my_family.is_18("Alex")

my_family.family_presentation()


# ---------------------------------------------------------------------------

# 🌟 Exercise 5 : TheIncredibles Family

# Create a class called TheIncredibles. This class should inherit from the Family class:
# This is no random family they are an incredible family, therefore the members attributes, will be a list of dictionaries containing the additional keys : power and incredible_name. (See Point 4)

# Add a method called use_power, this method should print the power of a member only if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.

# Add a method called incredible_presentation which :

# Print a sentence like “*Here is our powerful family **”
# Prints the family’s last name and all the members’ details (ie. use the super() function, to call the family_presentation method)
class TheIncredibles(Family):
    def __init__(self, last_name):
        super().__init__(last_name)
        self.members = []

    def use_power(self, name):
        for m in self.members:
            if m.get('name') == name:
                if m.get('age') >= 18:
                    print(f"{name} is using their power: {m['power']}!")
                else:
                    raise Exception(f"{name} is not over 18 and cannot use their power!")
                return
        print(f"{name} is not a member of the family.")

    def incredible_presentation(self):
        print(f"Here is our powerful {self.last_name} family!")
        for m in self.members:
            print(f"Name: {m['name']}, Age: {m.get('age', 'Unknown')}, Power: {m['power']}, "
                  f"Incredible Name: {m['incredible_name']}, Is Child: {m['is_child']}")

incredibles = TheIncredibles("Incredibles")

incredibles.members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
]

incredibles.incredible_presentation()

incredibles.born(name="Baby Jack", age=0, gender="Male", power="Unknown Power", incredible_name="BigJack")

incredibles.incredible_presentation()

incredibles.use_power('Michael')
incredibles.use_power('Sarah')
incredibles.use_power('Baby Jack')
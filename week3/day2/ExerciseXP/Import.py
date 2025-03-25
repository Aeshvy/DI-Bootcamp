from ExerciseXP import Dog
import random

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

class PetDog(Dog):
    def __init__(self, name, age, weight, trained = False):
        super().__init__(name, age, weight)
        self.trained = trained
    
    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dog_names = ", ".join([self.name] + [dog.name for dog in args])
        print(f'{dog_names} all play together.')

    def do_a_trick(self):
        if self.trained:
            
            tricks = [
                f'{self.name} does a barrel roll.',
                f'{self.name} stands on his back legs.',
                f'{self.name} shakes your hand.',
                f'{self.name} plays dead.'
            ]
            print(random.choice(tricks))
        else:
            print(f'{self.name} needs to be trained!')

dog1 = PetDog("Bark", 3, 20)
dog2 = PetDog("Dark", 2, 25)
dog3 = PetDog("Lucy", 4, 18)

dog1.train()
# dog2.train()
# dog3.train()

dog1.do_a_trick()
# dog2.do_a_trick()
# dog3.do_a_trick()

dog1.play(dog2, dog3)
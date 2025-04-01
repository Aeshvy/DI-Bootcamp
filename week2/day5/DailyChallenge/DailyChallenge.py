# Instructions : Old MacDonald’s Farm

# Create the code that is needed to receive the result provided above. Below are a few questions to assist you with your code:

# Does the Farm class need an __init__ method? If so, what parameters should it take?
# How many methods does the Farm class need?
# Do you notice anything interesting about the way we are calling the add_animal method? What parameters should this function have? How many…?
# Test your code and make sure you get the same results as the example above.
# Bonus: nicely line the text in columns as seen in the example above. Use string formatting.

# Create a class called Farm. How should it be implemented?

class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal, count = 1):
        if animal in self.animals:
            self.animals[animal] += count
        else:
            self.animals[animal] = count

    def get_info(self):
        info = f"{self.name}'s farm\n"
        for animal, count in self.animals.items():
            info += f"{animal} : {count}\n"
        return info.strip()
    
    # Add a method called get_animal_types to the Farm class. This method should return a sorted list of all the animal types (names) in the farm. With the example above, the list should be: ['cow', 'goat', 'sheep'].
    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animal_types = self.get_animal_types()
        animal_strings = [
            f"{animal}s" if self.animals[animal] > 1 else animal
            for animal in animal_types
        ]
        return f"{self.name}'s farm has " + ", ".join(animal_strings) + "."

macdonald = Farm("McDonald")

macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

print(macdonald.get_animal_types())
print(macdonald.get_info())
print(macdonald.get_short_info())
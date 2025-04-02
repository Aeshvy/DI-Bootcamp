import math, turtle

# Daily Challenge - Circle

# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.
# Bonus (not mandatory) : Install the Turtle module, and draw the sorted circles


class Circle:
    def __init__(self, radius=None, diameter=None):
        self.radius = radius if radius is not None else diameter / 2

    @property    
    def diameter(self):
        return self.radius * 2
    
# Compute the circle’s area
    @property
    def area(self):
        return f"{math.pi * self.radius ** 2:.2f}"              # area = π * r^2

# Print the attributes of the circle - use a dunder method
    def __str__(self):
        return f"Circle(radius={self.radius}, diameter={self.diameter})"
    
# Be able to add two circles together, and return a new circle with the new radius - use a dunder method
    def __add__(self, other):
        return Circle(self.radius + other.radius) if isinstance(other, Circle) else False
    
# Be able to compare two circles to see which is bigger, and return a Boolean - use a dunder method
    def __lt__(self, other):
        return self.radius < other.radius if isinstance(other, Circle) else False
    
# Be able to compare two circles and see if there are equal, and return a Boolean- use a dunder method
    def __eq__(self, other):
        return self.radius == other.radius if isinstance(other, Circle) else False

    def __repr__(self):
        return f"Circle (radius={self.radius}, diameter={self.diameter})"

circle1 = Circle(radius=5)
circle2 = Circle(diameter=12)
circle3 = Circle(radius=16)

print(f'Circle Area: {circle1.area}')

print(circle1)
print(circle2)

circle4 = circle1 + circle2
print(circle4)

print(circle1 < circle3)
print(circle1 == circle2)

# Be able to put them in a list and sort them
circle_list = [circle1, circle2, circle3]
sorted_circles = sorted(circle_list)
print(circle_list)


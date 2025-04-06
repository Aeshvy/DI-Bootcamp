# ✅ Part 1 : Quizz :
# Answer the following questions

# 1. What is a class?
# 2. What is an instance?
# 3. What is encapsulation?
# 4. What is abstraction?
# 5. What is inheritance?
# 6. What is multiple inheritance?
# 7. What is polymorphism?
# 8. What is method resolution order or MRO?

# 1. Template for creating objects with different attributes.
# 2. An object created from a class.
# 3. Hiding internal details (choosing what to display).
# 4. Display only features while hiding the back-end.
# 5. Enables a class to mimic (inherit) properties from a parent class.
# 6. Inheriting from more than one parent class.
# 7. Enables equal (same) behavior to differennt classes.
# 8. Pythonic order in which a method is looked for in a hierarchy.

# ✅ Part 2: Create a deck of cards class.

import random

class Card:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        self.shuffle()

    def shuffle(self):
        self.cards = [Card(suit, value) for suit in Card.suits for value in Card.values]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop() if self.cards else None

    def remaining_cards(self):
        return len(self.cards)

deck = Deck()
print("Dealing a card:", deck.deal())
print("Cards left:", deck.remaining_cards())

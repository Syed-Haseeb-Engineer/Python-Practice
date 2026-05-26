# PRACTICE THIS: session8_oop_advanced.py
import random # Required for Deck of Cards shuffling

print("=== Session 8: Static Attributes & Aggregation ===")

# --- Q1: Instance Counter ---
class Car:
    # [CONCEPT UNLOCKED: Static/Class Variable] -> Belongs to the class, not the object!
    counter = 0 
    
    def __init__(self):
        Car.counter += 1

c1 = Car()
c2 = Car()
c3 = Car()
print(f"Total Cars Created: {Car.counter}\n")


# --- Q2: Deck of Cards (Aggregation) ---
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    # [CONCEPT UNLOCKED: __str__ Magic Method] -> Controls what prints when you print() the object
    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        
        # [CONCEPT UNLOCKED: Aggregation] -> A Deck "HAS-A" list of Cards
        self.cards = [Card(s, v) for s in suits for v in values]
        self.shuffle()
        
    def shuffle(self):
        random.shuffle(self.cards)
        
    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        return "No cards left"
        
    def __str__(self):
        return f"Cards remaining in deck: {len(self.cards)}"

my_deck = Deck()
print(f"Dealt: {my_deck.deal()}")
print(my_deck)


# --- Q6 & Q7: Ice Cream Bowl (Advanced Aggregation) ---
class Scoop:
    def __init__(self, flavor, price):
        self.flavor = flavor
        self.__price = price # Private
        self.no_of_scoops = 1
        
    # Getters and Setters
    def get_price(self):
        return self.__price
        
    def set_price(self, new_price):
        self.__price = new_price

class Bowl:
    def __init__(self, max_scoops=3):
        self.__scoop_list = []
        self.max_scoops = max_scoops
        
    def add_scoops(self, *scoops):
        for scoop in scoops:
            if len(self.__scoop_list) < self.max_scoops:
                self.__scoop_list.append(scoop)
                print(f"{scoop.flavor} added!")
            else:
                print("Bowl is full!")
                
    def display(self):
        total = 0
        print("\n--- Bowl Contents ---")
        for scoop in self.__scoop_list:
            print(f"Flavor: {scoop.flavor} | Price: Rs.{scoop.get_price()}")
            total += scoop.get_price()
        print(f"Total Price: Rs.{total}")

# Execution
choco = Scoop("Chocolate", 50)
vanilla = Scoop("Vanilla", 40)
strawberry = Scoop("Strawberry", 45)
mint = Scoop("Mint", 55)

my_bowl = Bowl()
my_bowl.add_scoops(choco, vanilla, strawberry, mint) # Mint should trigger "Bowl is full!"
my_bowl.display()
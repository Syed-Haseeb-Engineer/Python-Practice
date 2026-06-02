# # PRACTICE THIS: session9_oop_architecture.py
# from abc import ABC, abstractmethod

# print("=== Session 9: Inheritance & Abstraction ===")

# # --- P1 & P2: Inheritance & Overriding (Vehicle/Bus) ---
# # [CONCEPT UNLOCKED: Inheritance (IS-A Relationship)]
# class Vehicle:
#     def __init__(self, seating_capacity):
#         self.seating_capacity = seating_capacity
        
#     def fare(self):
#         return self.seating_capacity * 100

# class Bus(Vehicle):
#     # Default capacity set to 50
#     def __init__(self, seating_capacity=50):
#         # [CONCEPT UNLOCKED: super()] -> Call the parent's __init__ method
#         super().__init__(seating_capacity)
        
#     def fare(self):
#         # Overriding the parent method to add 10% maintenance charge
#         base_fare = super().fare() 
#         return base_fare + (base_fare * 0.10)

# my_bus = Bus()
# print(f"Bus Fare for {my_bus.seating_capacity} seats: Rs.{my_bus.fare()}")


# # --- P3: Point and Location (Aggregation + Math) ---
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# class Location:
#     def __init__(self, source, destination):
#         self.source = source # Point object
#         self.destination = destination # Point object
        
#     def reflection_on_x_axis(self):
#         # Reflection on X-axis means the Y coordinate flips its sign
#         print(f"Destination Reflection: ({self.destination.x}, {-self.destination.y})")

# loc = Location(Point(0,0), Point(5, 10))
# loc.reflection_on_x_axis()


# # --- P4: Abstraction (Polygon) ---
# # [CONCEPT UNLOCKED: Abstract Base Classes (ABC)] -> Forcing children to implement methods!
# class Polygon(ABC):
#     @abstractmethod
#     def get_dimensions(self):
#         pass
        
#     @abstractmethod
#     def calculate_area(self):
#         pass

# class Triangle(Polygon):
#     def get_dimensions(self, base, height):
#         self.base = base
#         self.height = height
        
#     def calculate_area(self):
#         return 0.5 * self.base * self.height

# class RectangleShape(Polygon):
#     def get_dimensions(self, length, width):
#         self.length = length
#         self.width = width
        
#     def calculate_area(self):
#         return self.length * self.width

# tri = Triangle()
# tri.get_dimensions(10, 5)
# print(f"Triangle Area: {tri.calculate_area()}")


# # --- Q6: FlexibleDict (Overriding Built-in Classes) ---
# # [CONCEPT UNLOCKED: Inheriting from built-in Python Data Structures]
# class FlexibleDict(dict):
#     def __getitem__(self, key):
#         try:
#             # First, try to get the item exactly as requested
#             return super().__getitem__(key)
#         except KeyError:
#             # If it fails, check if we should swap string/int
#             if type(key) == str and key.isdigit():
#                 return super().__getitem__(int(key))
#             elif type(key) == int:
#                 return super().__getitem__(str(key))
            
#             # If it still fails, raise the error normally
#             raise KeyError(key)

# print("\n--- Testing FlexibleDict ---")
# fd = FlexibleDict()
# fd[1] = "Apple"
# fd["2"] = "Banana"

# # Accessing int key with string, and string key with int!
# print(f"Accessing key '1' (str): {fd['1']}") 
# print(f"Accessing key 2 (int): {fd[2]}")
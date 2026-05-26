# PRACTICE THIS: session7_oop_basics.py

print("=== Session 7: Classes and Objects ===")

# --- Q1: Rectangle Class ---
# [CONCEPT UNLOCKED: class & __init__]
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def perimeter(self):
        return 2 * (self.length + self.width)
        
    def area(self):
        return self.length * self.width
        
    def display(self):
        print(f"The length of rectangle is: {self.length}")
        print(f"The width of rectangle is: {self.width}")
        print(f"The perimeter of rectangle is: {self.perimeter()}")
        print(f"The area of rectangle is: {self.area()}\n")

my_rectangle = Rectangle(3, 4)
my_rectangle.display()

# --- Q2: Bank Account ---
class BankAccount:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            
    def withdrawal(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds or invalid amount.")
            
    def bank_fees(self):
        # Apply 5% fee
        fee = self.balance * 0.05
        self.balance -= fee
        
    def display(self):
        print(f"Account: {self.account_number} | Owner: {self.name} | Balance: Rs.{self.balance:.2f}\n")

account = BankAccount(101, "Nitish", 1000)
account.deposit(500)
account.withdrawal(200)
account.bank_fees()
account.display()

# --- Instructor Eligibility Task ---
class Instructor:
    def __init__(self, name, technology_skill, experience, avg_feedback):
        # [CONCEPT UNLOCKED: Private Variables (Double Underscore __)]
        self.__name = name
        self.__technology_skill = technology_skill # This should be a list
        self.__experience = experience
        self.__avg_feedback = avg_feedback
        
    def check_eligibility(self):
        if self.__experience > 3 and self.__avg_feedback >= 4.5:
            return True
        elif self.__experience <= 3 and self.__avg_feedback >= 4.0:
            return True
        return False
        
    def allocate_course(self, technology):
        if self.check_eligibility() and (technology in self.__technology_skill):
            return True
        return False

# Testing the Instructor
inst = Instructor("Ravi", ["Python", "Machine Learning"], 4, 4.8)
print(f"Eligible for Python? {inst.allocate_course('Python')}")
print(f"Eligible for Java? {inst.allocate_course('Java')}")

print("=== Session 1: Python Fundamentals ===")
    
# Q1: Print formatting using 'sep' 
print("\n--- Q1: Print Separator ---")
print("Data", "Science", "Mentorship", "Program", "started", "By", "CampusX", sep="-")
    
# Q2: Celsius to Fahrenheit
print("\n--- Q2: Temperature Conversion ---")
# Using float() for explicit type conversion
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit.")
    
# Q3: Swap without special syntax (a, b = b, a)
print("\n--- Q3: Swap Numbers (Algorithmic) ---")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"Before swap: num1 = {num1}, num2 = {num2}")
    
# Using a temporary variable (Standard algorithmic swap)
temp = num1
num1 = num2
num2 = temp
print(f"After swap: num1 = {num1}, num2 = {num2}")
    
# Q4: Euclidean distance (No 'math' module allowed yet!)
print("\n--- Q4: Euclidean Distance ---")
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
    
# Formula: √((x2-x1)² + (y2-y1)²)
# We use the arithmetic exponentiation operator (**) for square root 
distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print(f"The Euclidean distance is: {distance}")
    
# Q5: Simple Interest
print("\n--- Q5: Simple Interest ---")
principal = float(input("Enter Principal amount: "))
rate = float(input("Enter Rate of interest: "))
time = float(input("Enter Time period: "))
    
simple_interest = (principal * rate * time) / 100
print(f"The Simple Interest is: {simple_interest}")
    
# Q6: Dogs and Chickens (Pure Math / Linear Algebra)
print("\n--- Q6: Dogs and Chickens ---")
total_heads = int(input("Enter total heads: "))
total_legs = int(input("Enter total legs: "))


# Visual: The Dogs & Chickens Equation (Problem 6)
# We solve this using simple linear algebra.
# Let $d$ = dogs, $c$ = chickens.
# Heads equation: $d + c = TotalHeads \Rightarrow c = TotalHeads - d$
# Legs equation: $4d + 2c = TotalLegs$
# Substitute $c$: $4d + 2(TotalHeads - d) = TotalLegs \Rightarrow 2d + 2(TotalHeads) = TotalLegs$
# Final Formula: $d = (TotalLegs - 2 \times TotalHeads) / 2$


# Dogs have 4 legs, chickens have 2. 
# Equation: dogs = (legs - (2 * heads)) / 2
# We use integer division (//) to return whole numbers 
dogs = (total_legs - (2 * total_heads)) // 2
chickens = total_heads - dogs
print(f"There are {dogs} dogs and {chickens} chickens.")
    
# Q7: Sum of squares of first n natural numbers
print("\n--- Q7: Sum of Squares ---")
n = int(input("Enter n: "))
    
# Formula: n(n+1)(2n+1)/6
sum_of_squares = (n * (n + 1) * (2 * n + 1)) // 6
print(f"Sum of squares up to {n} is: {sum_of_squares}")

# Q8: Nth term of Arithmetic Series
print("\n--- Q8: AP Nth Term ---")
first_term = float(input("Enter 1st term: "))
second_term = float(input("Enter 2nd term: "))
n_term = int(input("Enter the value of N: "))
    
common_difference = second_term - first_term
# Formula: a + (n-1)d
nth_term = first_term + (n_term - 1) * common_difference
print(f"The {n_term}th term is: {nth_term}")
    
# Q9: Sum of fractions (No 'fractions' module allowed yet!)
print("\n--- Q9: Sum of Two Fractions ---")
n1 = int(input("Enter numerator 1: "))
d1 = int(input("Enter denominator 1: "))
n2 = int(input("Enter numerator 2: "))
d2 = int(input("Enter denominator 2: "))
    
# Cross multiplication logic
result_num = (n1 * d2) + (n2 * d1)
result_den = d1 * d2
print(f"The sum is: {result_num}/{result_den}")
    
# Q10: Milk Tank Volume
print("\n--- Q10: Milk Tank Capacity ---")
# Using 3.14 as a float literal for pi, since we can't import math yet 
pi_literal = 3.14 
    
H = float(input("Enter Tank Height (cm): "))
L = float(input("Enter Tank Length (cm): "))
B = float(input("Enter Tank Breadth (cm): "))
    
h_glass = float(input("Enter Glass Height (cm): "))
r_glass = float(input("Enter Glass Radius (cm): "))
    
tank_volume = H * L * B
glass_volume = pi_literal * (r_glass ** 2) * h_glass
    
# We use integer division (//) because we can only have whole glasses of milk 
total_glasses = int(tank_volume // glass_volume)
print(f"You can obtain {total_glasses} full glasses of milk.")


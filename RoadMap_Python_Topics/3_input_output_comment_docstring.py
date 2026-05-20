#%%
def calculate_birth_year(age):
    """
    Calculates an approximate birth year based on a given age.

    Arguments:
    age (int):
    The user's age in years.

    Returns:
    int: The calculated birth year (assuming the current year is 2026). 
    """
    #Note: we are hardcoding the year for this example.
    current_year = 2026
    birth_year = current_year - age
    return birth_year


#1.Output section
print("=== Ubuntu User Profiler ===")

#2.Get Input (This always returns a string!)
user_name = input("Enter your username: ")
age_input = input(f"Hello {user_name}, enter your age:")

#3.Type Casting
user_age = int(age_input)

#4. Use our documented function
calculated_year = calculate_birth_year(user_age)

#5.Output the final result
print("\n--- Profile Summary ---")
print(f"User: {user_name}")
print(f"Estimated Birth Year: {calculated_year}")

#How to view a Docstring in code!
#The __doc__ attribute lets us print the manual for our function directly.
print("\n--- Function Documentation ---")
print(calculate_birth_year.__doc__)

# %%
#Operators
# integer operatos
print(11//2)
print(11/2)


#bitwise operators (it performce on bit level)


#bitwise AND
print(2 & 3)
#Binary number for 2 =         10
#Binary number for 3 =         11 
#Binray number for result(2) = 10

#bitwise OR
print(2 | 3)
#Binary number for 2 =         10
#Binary number for 3 =         11 
#Binray number for result(3) = 11

#bitwise XOR (if both numbers are same then 0 if not 1)
print(2 ^ 3) 
#Binary number for 2 =         10
#Binary number for 3 =         11 
#Binray number for result(3) = 01

#bitwise NOT
print(~3)
#Binary number for 3 = 11
#Binary number for result = 


#Membership operator
print('D' in 'Delhi')
print('D' not in 'Delhi')


# %%
#WAP to take input from user as 3 digit and sum the given digits
number = int(input('Enter 3 digit number'))
Result = 0

while number > 0:
    Result += number % 10
    number = number//10


print(Result)
# %%

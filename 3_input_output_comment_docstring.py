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

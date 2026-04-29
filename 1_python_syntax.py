#%%
greeting="Hello,Ubuntu User!"
if True:
    print(greeting)
    print("This line is inside the 'if' block")

print("This line is outside ther 'if' block, back at the normal level.")

#%%
user_age = 25
coffee_price = 4.50
os_name = "Ubuntu"

is_leaning_python = True
mystery_variable = 100
print("Mystery is currently a number:", mystery_variable)

mystery_variable = "Now i am a string"
print("Mystery is now text", mystery_variable)


# %%
server_status = "offline"

if server_status == "online":
    print("Server is running perfectly")
elif server_status == "rebooting":
    print("Please wait, server is coming up.")
else:
    print("Critical: server is offline")

#%%
print("\n Initiating Server restart sequence")
for i in range(3):
    print("Attempting restart... count", i)

#%%
battery_level = 3
while battery_level > 0:
    print("Battery level at:", battery_level)
    battery_level -=1

print("Battery depleted")


#%%
def calculate_server_load(users, processes_per_user):
    """This string is a docstring. It explains what the function does."""
    total_processes = users * processes_per_user

    if total_processes > 1000:
        return "WARNING: High load"
    else:
        return "System Stable"
    
status1 = calculate_server_load(50,10)
status2 = calculate_server_load(200,6)

print("Server 1 Status:", status1)
print("Server 2 Status:", status2)


#Lambda: A quick, 1-line function.
#syntax lambda arguments: expression
multiply = lambda a,b: a * b
print("\n Lambda test (5 * 4):", multiply(5,4))


#%%
def math_operation(num1, num2, operator):
    if operator == "add":
        return (num1+num2)
    elif operator == "subtract":
        return (num1-num2)
    elif operator == "multiply":
        return (num1*num2)
    elif operator == "divide":
        return (num1/num2)
    elif operator == "modulus":
        return (num1%num2)
    else:
        print("This is invalid operator")


num1 = 20  
num2 = 10

addition = math_operation(num1,num2,"add")
subtraction = math_operation(num1,num2,"subtract")
multiplication = math_operation(num1,num2,"multiply")
division = math_operation(num1,num2,"divide")
modulus = math_operation(num1,num2,"modulus")


print("The addition is", addition)
print("The subtraction is", subtraction)
print("The Multiplication is", multiplication)
print("The division is", division)
print("The Modulus is", modulus)# %%

# %%

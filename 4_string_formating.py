ubuntu_version = 24.04
username = "linux_learner"

old_way = "user %s is running Ubuntu version %.2f" % (username, ubuntu_version)
print("old Way:", old_way)


middle_way = "User {} is running Ubuntu version {}" .format(username, ubuntu_version)
print("Middle Way:", middle_way)

modern_way = f"User {username} is running Ubuntu version {ubuntu_version}"
print("Modern Way:", modern_way)


# in f string we can perform operation inside curly braces
print(f"Next year, you will upgrade to Ubuntu {ubuntu_version + 2.0}")

#%%
#Diffent types of string creation
s= 'hello'
s= "hello"
s= '''hello'''
s= """hello"""

#%%
#Program on factorial
n = int(input("Enter the number for which you required factorial"))

result = 0
fact = 1

for i in range(1,n+1):
    fact = fact * i
    #result = result + i/fact

print(fact)
# %%
for i in range(1,5):
    for j in range(1,5):
        print(i,j)
        
# %%
for i in range(1,5):
    for j in range(1,i+1):
        print("*", end = "")
    
    print("\n")
# %%

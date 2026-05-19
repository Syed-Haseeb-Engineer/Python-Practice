#%%
#WAP to guess random number
import random

jackpot = random.randint(1,100)

guess = int(input("Guess the value"))
counter = 1

while guess != jackpot:
    if guess < jackpot:
        print('ghalat! guess higher')
    else:
        print('ghalat! guess lower')

    
    guess = int(input('guess karo'))
    counter += 1

#to just understand else work with loops as well
else:
    print("correct guess")
    print("Attempts", counter)

#Instead of above i can use this below as well
# print("correct guess")
# print("Attempts", counter)



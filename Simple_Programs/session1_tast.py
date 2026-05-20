#%%print the given strings as per stated format

print("Data","Science", "Mentorship", "By", "Campusx", sep= '-')


# %%
celcius = 25
fahrehneit = (celcius * 9/5) + 32
print(fahrehneit)


# %%
a = 10
b = 20
print(a,b)
a = a + b
b = a - b
a = a - b
print(a,b)

# %%
import math
p1, p2 = (0,0), (3,4)
distance = math.dist(p1,p2)
print(distance)


# %%
heads, legs = 10,20
dogs = (legs-(2*heads))//2
chicken = heads - dogs
print(dogs,chicken)
# %%
n = int(input("enter the nth number for which you want sum of n natural numbers"))
for i in range(0,n):
    sum += i

print(sum)
# %%

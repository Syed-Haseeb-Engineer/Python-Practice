#%%
s = "Syed Haseeb"
count = 0 
for i in s:
    count += 1


print("The lenth of {} is {}".format(s,count))

#%%
email = input("Enter your mail")
pos = email.index('@')
print(email[0:pos])

# %%
n = input("Enter the string")
s = input("Enter the character you want to search")
count =0 
for i in n:
    if i==s:
        count += 1
print(count)


# %%
s = "Syed Hasee2b"
r = '2'
result = ''
for i in s:
    if i != r:
        result= result + i

print(result)

# %%
# s = 'malayalam'
s = input("enter a string")

# the below code is by me
# # s = input("enter a string")
# if s[0:] == s[::-1]:
#     print("{} is palindrome".format(s))
# else:
#     print("{} is not a palindrome". format(s))

#The below code is my nitish
flag = True
for i in range(0,len(s)//2):
    if s[i]!= s[len(s)-i-1] :
        print("{} is palindrome".format(s))
        flag = False
if flag:
    print("{} is palindrome".format(s))

# %%
s = "My Name Is Syed Haseeb"
count = 1
for i in s:
    if i == ' ':
        count += 1
print(count)


# %%
s = "syed haseeb"
l = []
for i in s.split():
    l.append(i[0].upper() + i[1:].lower())
print(l)
# %%

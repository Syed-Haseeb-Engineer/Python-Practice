#%%
ram_gb = 16
kernel_version = 6.8
distro_name = "Ubuntu"

print(f"ram_gb is {ram_gb} | Type: {type(ram_gb)}")
print(f"kernel_version {kernel_version} | Type: {type(kernel_version)}")
print(f"distro_name {distro_name} | Type: {type(distro_name)}")


simulated_file_input = "500"

clean_number = int(simulated_file_input)
print(8)
print(1e308) # python supporst 1*10^308
print(1e309)
print(f"\nCasted to integer: {clean_number} | New Type: {type(clean_number)}")

print(f"Math works now: {clean_number + 50}")

precise_number = float(clean_number)
print(8.55)
print(1.7e308)
print(1.7e308) # it will give infinite because it doesn't support 
print(f"casted to float: {precise_number} | New Type: {type(precise_number)}")

version_text = str(kernel_version)
print(f"Casted back to string: '{version_text}' | New Type: {type(version_text)}")


#complex
print(5+6j)



#variables
# in python we use dynamic typing which means we dont need to specify variable type 

name = 'Syed Haseeb'
print(name)

#Dynamic Binding means the variable can hold different data type values
a = 5
print(a)

a = "Syed Haseeb"
print(a)

#Assigning values to variables by different methods
a,b,c=1,2,3 # assigning different values to different variables 
print(a,b,c)

a=b=c=5 # assigning 5 to all variables
print(a,b,c)


#small program to take two inputs from user and result the addition
#%%
fnum = input("Enter firs number")
snum = input("Enter Second Number")
print(type(fnum), type(snum))
result = fnum + snum
print(result) # because python store everything in string we received 5667 as its adds the string

# now we will convert/ type cast to int
result = int(fnum) + int(snum)
print(result)
print(type(fnum)) # type convertion or explicit type casting cant change its variable permenantly just it will conver the same object and return to the new one

#The main difference between type casting and type conversion is 
#Type casting me the original variable data type will change
#Type conversion means it will not change original variable type. this is used in python


# %%

#Literal

a = 0b1010 # binary literals
b = 100 # Decimal Literals
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#float litera
float_1 = 10.5
float_2 = 1.5e2   #1.5 * 10^2
float_3 = 1.5e-3  #1.5 * 10^-3

#complex literal
x = 3.14j

print(a,b,c,d) # for integer literal
print(float_1, float_2, float_3) # for float literal
print(x,x.imag, x.real) # for complex literal

# %%
# string
string = 'This is python'
strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than line code."""
unicode = u"\U0001f600\U0001F606\U0001F923"
raw_str = r"raw \n string"

print(string)
print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)


# %%
#operation on boolean
a = True + 4
b = False + 10
print("a:", a) #Added 4 on True (which is 1) 1 + 4 =  5
print("b:", b) #Added 10 on False (which is 0) 0 + 10 = 10
# %%

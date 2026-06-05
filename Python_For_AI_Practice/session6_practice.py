# def is_even(num):
#     """
#     This function returns if a given number is odd or even
#     input - any valid integer
#     output - odd/even
#     created on - 16th Nov 2022
#     """
#     if type(num) == int:
#         if num % 2 == 0:
#             return 'even'
#         else:
#             return 'odd'
#     else:
#         return 'pagal hai kya?'

# print(is_even.__doc__)

# def g(y):
#     print(x)
#     print(x+1)
# x = 5
# g(x)
# print(x)

# def f(y):
#     x = 1
#     x += 1
#     print(x)
# x = 5
# f(x)
# print(x)

# def h(y):
#     x += 1
# x = 5
# h(x)
# print(x)

# def f(x):
#     x = x + 1
#     print('in f(x): x =', x)
#     return x
# x = 3
# z = f(x)
# print('in main program scope: z =', z)
# print('in main program scope: x =', x)

# def g(x):
#     def h():
#         x = 'abc'
#     x = x + 1
#     print('in g(x): x =',x)
#     h()
#     return x
# x = 3
# z = g(x)
# print(x)
# print(z)
# def square(num):
#   return num**2

# type(square)

# id(square)
# L = [1,2,3,4,square]
# print(L)
# print(L[-1](3))
# print(L)

# def f():
#     def x(a, b):
#         return a+b
#     return x
    
# val = f()(3,4)
# print(val)

# def cube(x):
#     return x ** 3
def transform(f,L):
    output = []
    for i in L:
        output.append(f(i))
    print(output)


L = [1,2,3,4]
transform(lambda x:x**2,L)

# def transform(f,L):
#   output = []
#   for i in L:
#     output.append(f(i))

#   print(output)

# L = [1,2,3,4,5]

# transform(lambda x:x**3,L)

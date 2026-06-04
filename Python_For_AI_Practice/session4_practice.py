
#list creation and memory address
# l = [1,[1,2],2,[1,[2,3,[1,5],2],5],1]        
# print(l)
# print(id(1))
# print(id(l))
# print(id(l[1]))



# #Indexing
# l= [[[1,2],[3,4]],[[5,6],[7,8]]]
# print(l[0][1][1])
# print(l[1],[0])
 
# #Negative Indexing
# print(l[-1][-2][-1])

# l1 = [1,2,3,4]
# l1[-1] = 500
# print(l1)
# l2 = [1,2,3,45] #it will compare every element and value
# print(l1 == l2)

# l= [[[1,2],[3,4]],[[5,6],[7,8]]]
# print(l[0:]) #what if i want to access sub elements using slicing



# l1 = [1,2,3,4]
# l1[-1] = 500
# print(l1)

# l1 = [1,2,3,4]
# l1.remove(3)
# print(l1)

# l3 = [[[1,2], [3,4]],[[5,6],[7,8]]]
# for i  in l3:
#     for j in range(i):
#         print(i,j) #how to traverse sub lists



#accessing the sub elements from list
# l3 = [[[1,2], [3,4]],[[5,6],[7,8]]]
# for i  in l3:
#     print(i[1][1])






# l = [2,1,5,7,0]
# print(sorted(l,reverse=True))


# l = [2,1,5,7,0]
# print(l)
# print(sorted(l))
# print(l)
# l.sort()
# print(l)


# l = [1,2,3,4]
# lsq = [i**2 for i in l]
# print(lsq)

# div_by_5 = [i for i in range(100) if i % 5 == 0]
# print(div_by_5)

# languages = ['php', 'sql', 'python','postgre','java']
# stat_p = [language for language in languages if language.startswith('p')]
# print(stat_p)


# #nested if with list comprehension
# basket = ['apple','guava','cheerry','banana']
# my_fruits = ['apple','kiwi','grapes','banana']

# new_list = [fruit for fruit in my_fruits if fruit in basket if fruit.startswith('a')]
# print(new_list)

# nested_list_comp = [[i*j for i in range(1,4)] for j in range(1,4)]
# print(nested_list_comp)


# #cartisan product
# l1 = [1,2,3,4]
# l2 = [5,6,7,8]
# cartisina_list = [i*j for i in l1 for j in l2]
# print(cartisina_list)


# l = [1,2,3,4,5,6]   #int 'object' is not iterable
# pl = []
# ol = []
# for i in l:
#     if i % 2 == 0:
#         pl.append(i)
#     else:
#         ol.append(i)

# print("Even list {} and Odd List {}".format(pl,ol))


# l = list(input("Enter a list"))
# print(l)

# l1 = [1,2,3,4]
# l2 = [5,6,7,8]
# # merge = l1 + l2
# # print(merge)
# m = []
# for i in l1:
#     m.append(i)
# for i in l2:
#     m.append(i)

# print(m)


# l = [1,2,3,4]
# for i in range(0,len(l)):
#     if l[i]!=3:
#         l[i] = l[i]
#     else:
#         l[i] = 200 

# print(l)


# l = [[1,3],[2,4],[5,1],[7,1]]
# l1d = []
# for i in l:
#     for j in i:
#         l1d.append(j)
# print(l)
# print(l1d)

# l = [1,2,1,2,3,4,5,3,4]
# r = []
# for i in l:
#     if i not in r:
#         r.append(i)
# print(l)
# print(r)

# l = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
# # Replace odd numbers with "Odd" and keep evens as-is
# transformed = ["Odd" if item % 2 != 0 else "Even" for block in l for row in block for item in row]
# print(transformed)
# # Output: ['Odd', 2, 'Odd', 4, 'Odd', 6, 'Odd', 8]

# l = [4,3,2,4]
# is_ascending = l== sorted(l)
# is_descenging = l == sorted(l, reverse= True) 

# if is_ascending:
#     print("asceding",l)
# elif is_descenging:
#     print("descending",l)
# else:
#     print(l,"list is unordered")

# l = [1,2,3,1]
# l1 = [1,3,2,1]
# print(l== l1)
# print(list('hello'))
# L = [2,1,5,7,0]
# print(L)
# print(id(L))
# L1 = L.copy()
# print(L1)
# print(id(L1))

# deep copy vs shallow copy 
# why immutable datatypes have less space and time
# and when we use del to delete string wheather it will permenantly deletes or just temporary. if temporary then why
# difference between pop and del, and why in tuple and list pop remove last element and in sets it removes first element

# import time
# import sys
# start = time.time()
# L = []
# for i in range(1,11):
#     L.append(i)
# print(L)
# print(sys.getsizeof(L))
# print(id(L))
# print("time taken using loop", time.time()-start)

# start = time.time()
# L1 = [i for i in range(1,11)]
# print(L1)
# print(id(L1))
# print(sys.getsizeof(L1))
# print("time taken using comprehension", time.time()-start)


# L1 = [1,2,3,4,5]
# L2 = [-1,-2,-3,-4]
# print(list(zip(L1,L2))).

L = [1,2,3,4,5,6]
l_odd = [i for i in range(len(L)+1) if i%2==0 ]
l_even = [i for i in range(len(L)+1) if i%2 == 1]

print(l_odd,l_even)
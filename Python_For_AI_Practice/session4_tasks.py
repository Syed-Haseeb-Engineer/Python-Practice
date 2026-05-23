#Questions
#1.



# print("\n === Session4 List and Comprehension ===")

# print("\n --- P1: List Addition ---")
# l1 = ["M", "na", "i","kh"]
# l2 = ["y","me","s","an", "a"]
# maxl = max(len(l1),len(l2))
# print(maxl)
# result = []
# for i in range(0,maxl):
#     if i < len(l1):
#         result.append(l1[i])
#     if i < len(l2):
#         result.append(l2[i])
# print(result)

# print("\n ---P2: Add 7000 after 6000 in list ----")
# l1 = [10,20,[300,400,[5000,6000],500],30,40]
# # l1[1][2].append(7000)

# for i in l1:
#     for j in range(4):
#         for k in range(4):
#             if (l1[i][j][k]) == (l1[2][2][3]):
#                 l1[i][j][k] = 7000
# print(l1)

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

l = [1,2,3,4]

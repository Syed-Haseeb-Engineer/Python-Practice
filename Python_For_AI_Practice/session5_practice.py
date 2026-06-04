# import time
# l = list(range(10000))
# t = tuple(range(10000))

# start = time.time()
# for i in l:
#     i*5
# print("List time",time.time()-start)

# for i in t:
#     i*5
# print("Tuple time",time.time()-start)


# import sys
# l = list(range(1000))
# t = tuple(range(1000))

# print("list of",sys.getsizeof(l))
# print("tuple of",sys.getsizeof(t))

# s1 = {1,2,3}
# s2 = {3,2,1}
# print(s1,s2)
# print(s1 == s2)

# s = {1,2,3,4,5}
# print(s)
# del s[0]
# s.discard(50) #it will handle error if element not found
# print(s)
# s.remove(40) #it will through error if element not found
# print(s)
# s.pop() #it will delete elements from front
# print(s)
# s.clear()
# print(s)


# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}
# print(s1 | s2)
# print(s1 & s2)
# print(s1-s2)
# print(s2-s1)
# print(s1 ^ s2)
# print(1 not in s1)
# for i in s1:
#     print(i,end=" ")

# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}

# # s1.union(s2)
# # s1.update(s2) # it will update the union and insert to s1.
# # print(s1)
# # print(s2)
# # print(s1.union(s2))
# # print(s1.update(s2))

# print(s1.intersection(s2))
# s1.intersection_update(s2)
# print(s1,s2)


# fs1 = frozenset([1,2,3])
# fs2 = frozenset([3,4,5])
# print(fs1 | fs2)

# d = {}
# print(d)
# s ={
#     'name':"Syed Haseeb",
#     'college': "Sophia",
#     "subjects": {
#         "dsa":50,
#         "maths": 60,
#         "python": 80
#     }
# }
# print(s)

# d5 = {'name':'haseeb','name':'nitish'}
# print(d5)

# d6 = {'name':'haseeb',(1,3,4):"tuple"}
# print(d6)

# my_dict = {'name': 'Jack', 'age': 26}
# print(my_dict['age'])
# print(my_dict.get('age'))
# print(s['subjects']['maths'])



# a = [1,2,3]
# b = a.copy()
# a.append(4)
# print(a)
# print(b)
# [1, 2, 3, 4]
# [1, 2, 3, 4]

# a = (1,2,3)
# b = a
# a = a + (4,)
# print(a)
# print(b)

# s = {1,2,3,4,5}
# s.push()
# print(s)

# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}
# # s1 | s2
# print(s1.union(s2))
# s1.update(s2)
# print(s1)
# print(s2)

# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}
# print(s1.intersection(s2))
# # s1.intersection_update(s2)
# print(s1)
# print(s2)


# s1 = {1,2,3,4,5}
# s2 = {3,4,5}
# print(s1.issuperset(s2))
# print(s2.issubset(s1))

# s1 = {1,2,3}
# s2 = s1.copy()
# print(s1.add(5))
# print(s1)
# print(s2)

# d5 = {'name':'nitish','name':'rahul'}
# print(d5)

# d6 = {'name':'nitish',(1,2,3):2}
# print(d6)

d = {'name': 'nitish', 'age': 32, 3: 3, 'gender': 'male', 'weight': 72}
# pop
print(d)
d.pop(3)
d.popitem()
del d['age']
print(d)


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
# l1[2][2].insert(2,7000)
# print(l1)

# candy_list = ['Jelly Belly','Kit kat','Double Bubble','Milky Way','Three Musketeers']
# print("\n P3:")
# no_of_items = [10,20,34,74,32]
# capacity = [(i,j) for i,j in zip(candy_list,no_of_items)]# print(capacity)



# print("\n P4: running sum of list")

# list1 = [1,2,3,4,5,6]
# result = 0
# for i in list1:
#     result = result + i
#     print(result,end=",")

l1 = [2,4,6,10,1]
result = []
for x in l1:
    suml = 0
    for y in l1:
        if y>=x:
            suml = suml + y
    result.append(suml)
print(result)

# res = [sum([y for y in l1 if y>=x]) for x in l1]
# print(res)


















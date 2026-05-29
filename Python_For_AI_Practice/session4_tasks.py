print("\n === Session4 List and Comprehension ===")

print("\n --- P1: List Addition ---")
l1 = ["M", "na", "i","kh"]
l2 = ["y","me","s","an", "a"]
maxl = max(len(l1),len(l2))
print(maxl)
result = []
for i in range(0,maxl):
    if i < len(l1):
        result.append(l1[i])
    if i < len(l2):
        result.append(l2[i])
print(result)

print("\n ---P2: Add 7000 after 6000 in list ----")
l1 = [10,20,[300,400,[5000,6000],500],30,40]
# l1[1][2].append(7000)
l1[2][2].insert(2,7000)
print(l1)

candy_list = ['Jelly Belly','Kit kat','Double Bubble','Milky Way','Three Musketeers']
print("\n P3:")
no_of_items = [10,20,34,74,32]
capacity = [(i,j) for i,j in zip(candy_list,no_of_items)]# print(capacity)



print("\n P4: running sum of list")

list1 = [1,2,3,4,5,6]
result = 0
for i in list1:
    result = result + i
    print(result,end=",")

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

# # PRACTICE THIS: session4_lists.py

# print("=== Session 4: Lists & Comprehensions ===")

# # --- P1: Combine two lists index-wise (with leftovers) ---
# print("\n--- P1: Combine Lists ---")
# list1 = ["M", "na", "i", "Kh"]
# list2 = ["y", "me", "s", "an", "Extra1", "Extra2"]
# result = []
# # [CONCEPT UNLOCKED: max() and len()] -> Find the longest list
# max_len = max(len(list1), len(list2))
# for i in range(max_len):
#     temp = []
#     if i < len(list1): temp.append(list1[i])
#     if i < len(list2): temp.append(list2[i])
#     result.append(temp)
# print(result)

# # --- P2: Add item after a specified item in a nested list ---
# print("\n--- P2: Nested List Insertion ---")
# l1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# # We hardcode the indexing because we know the structure (No recursive functions allowed yet!)
# l1[2][2].insert(2, 7000) # [CONCEPT UNLOCKED: list.insert(index, element)]
# print(l1)

# # --- P3: Update no of items available ---
# print("\n--- P3: Candy Inventory ---")
# candy_list = ['Jelly Belly', 'Kit Kat', 'Double Bubble']
# no_of_items = [10, 20, 34]
# # [CONCEPT UNLOCKED: zip()] -> Iterate multiple lists simultaneously
# for candy, count in zip(candy_list, no_of_items):
#     print(f"{candy}-{count}")

# # --- P4: Running Sum on list ---
# print("\n--- P4: Running Sum ---")
# nums = [1, 2, 3, 4, 5, 6]
# running_sum = []
# current_total = 0
# for n in nums:
#     current_total += n
#     running_sum.append(current_total)
# print(running_sum)

# # --- P5: Sum of elements greater and itself ---
# print("\n--- P5: Conditional Sum ---")
# nums2 = [2, 4, 6, 10, 1]
# # [CONCEPT UNLOCKED: Nested List Comprehension]
# res = [sum([y for y in nums2 if y >= x]) for x in nums2]
# print(res)

# # --- P6: Common unique items (Increasing Order) ---
# # Note: Cannot use Sets yet! Must use List logic.
# print("\n--- P6: Common Unique ---")
# num1 = [23, 45, 67, 78, 89, 34, 34]
# num2 = [34, 89, 55, 56, 39, 67]
# common = []
# for n in num1:
#     # [CONCEPT UNLOCKED: 'in' operator for membership]
#     if (n in num2) and (n not in common):
#         common.append(n)
# common.sort() # [CONCEPT UNLOCKED: list.sort()]
# print(common)

# # --- P7: Sort alphanumeric strings based on product value ---
# # We cannot use custom sorting functions yet, so we use a clever List of Lists trick!
# print("\n--- P7: Product Sort ---")
# strings = ['lac21', '23fg', '456', '098d', '1', 'kls']
# sorting_list = []
# for s in strings:
#     prod = 1
#     has_digit = False
#     for char in s:
#         if char.isdigit(): # [CONCEPT UNLOCKED: string.isdigit()]
#             prod *= int(char)
#             has_digit = True
#     if not has_digit: prod = 1
#     # We append [product, string]. Python's .sort() will sort by the first item (product)!
#     sorting_list.append([prod, s])

# sorting_list.sort()
# final_sorted_strings = [item[1] for item in sorting_list]
# print(final_sorted_strings)

# # --- P8 to P10: String/List splits and formatting ---
# print("\n--- P8-P10: Formatting ---")
# # P8: Split on space and hyphen
# raw = ['CampusX is a channel', 'for data-science']
# # Replace hyphens with spaces, then split!
# p8_res = " ".join(raw).replace("-", " ").split()
# print("P8:", p8_res)

# # P9: Matrix to String
# matrix_char = [['c','a','m'], ['p','u','x']]
# p9_res = "".join([char for row in matrix_char for char in row])
# print("P9:", p9_res)

# # P10: Add space before capital letters
# camel_words = ['campusxIs', 'bestFor']
# p10_res = []
# for word in camel_words:
#     new_word = "".join([" " + c if c.isupper() else c for c in word])
#     p10_res.append(new_word.strip())
# print("P10:", p10_res)

# # --- P11 to P15: Advanced List Comprehensions & Matrices ---
# print("\n--- P11-P15: Comprehensions ---")
# l_a, l_b = [1,2,3,4,5,1], [2,3,5,7,8]
# union_list = l_a + [x for x in l_b if x not in l_a]
# print("P11 Union:", union_list)

# mat = [[1,2,3], [4,5,6], [7,8,9]]
# print("P12 Row Maxes:", [max(row) for row in mat])
# print("P13 Gen Matrix:", [[j for j in range(i, i+3)] for i in range(0, 9, 3)])
# print("P14 Transpose:", [[row[i] for row in mat] for i in range(len(mat[0]))])
# print("P15 Flatten:", [item for row in mat for item in row])

# # === SESSION 4: LISTS ===

# # P1: Combine two lists index-wise (with leftovers)
# l1 = ["M", "na", "i", "Kh"]
# l2 = ["y", "me", "s", "an", "Extra"]
# combined = []
# for i in range(max(len(l1), len(l2))):
#     temp = []
#     if i < len(l1): temp.append(l1[i])
#     if i < len(l2): temp.append(l2[i])
#     combined.append(temp)
# print("P1:", combined)

# # P2: Add item to nested list after specified item
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# # [CONCEPT UNLOCKED: list.index()]
# target_idx = list1[2][2].index(6000)
# list1[2][2].insert(target_idx + 1, 7000)
# print("P2:", list1)

# # P3: Candy Inventory (Zip)
# candy = ['Jelly Belly', 'Kit Kat', 'Double Bubble', 'Milky Way', 'Three Musketeers']
# items = [10, 20, 34, 74, 32]
# print("P3:")
# for c, i in zip(candy, items):
#     print(f"{c}-{i}")

# # P4: Running Sum
# nums = [1, 2, 3, 4, 5, 6]
# run_sum = []
# total = 0
# for n in nums:
#     total += n
#     run_sum.append(total)
# print("P4:", run_sum)

# # P5: Add all elements greater and itself
# nums2 = [2, 4, 6, 10, 1]
# res = [sum([y for y in nums2 if y >= x]) for x in nums2]
# print("P5:", res)

# # P6: Common unique items in increasing order (NO SETS ALLOWED YET)
# num1 = [23, 45, 67, 78, 89, 34, 34]
# num2 = [34, 89, 55, 56, 39, 67]
# common = []
# for n in num1:
#     if n in num2 and n not in common:
#         common.append(n)
# common.sort()
# print("P6:", common)

# # P7: Sort alphanumeric strings based on product value
# strings = ['lac21', '23fg', '456', '098d', '1', 'kls']
# sorting_list = []
# for s in strings:
#     prod = 1
#     has_digit = False
#     for char in s:
#         if char.isdigit():
#             prod *= int(char)
#             has_digit = True
#     if not has_digit: prod = 1
#     sorting_list.append([prod, s])
# sorting_list.sort()
# print("P7:", [item[1] for item in sorting_list])

# # P8: Split on space and hyphen
# raw = ['CampusX is a channel', 'for data-science', 'aspirants.']
# # Replace hyphen with space, then split the joined string
# p8_res = " ".join(raw).replace("-", " ").split()
# print("P8:", p8_res)

# # P9: Char Matrix to String (Comprehension)
# mat = [['c', 'a', 'm', 'p', 'u', 'x'], [' ', 'i', 's'], [' ', 'b', 'e', 's', 't']]
# p9_res = "".join([char for row in mat for char in row])
# print("P9:", p9_res)

# # P10: Add Space before Capital Letters
# camel = ['campusxIs', 'bestFor', 'dataScientist']
# p10_res = ["".join([" " + c if c.isupper() else c for c in word]).strip() for word in camel]
# print("P10:", p10_res)

# # P11: Union of 2 lists
# l_a, l_b = [1,2,3,4,5,1], [2,3,5,7,8]
# union = l_a + [x for x in l_b if x not in l_a]
# print("P11:", union)

# # P12-P15: Matrix Comprehensions
# matrix = [[1,2,3], [4,5,6], [7,8,9]]
# print("P12 Row Max:", [max(row) for row in matrix])
# print("P13 Gen Matrix:", [[j for j in range(i, i+3)] for i in range(0, 9, 3)])
# print("P14 Transpose:", [[row[i] for row in matrix] for i in range(len(matrix[0]))])
# print("P15 Flatten:", [item for row in matrix for item in row])














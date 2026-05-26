# print("=== Session 5: Tuples, Sets, Dictionaries ===")
# print("\n --- Tuple Tasks ---")
# t_list = [(5,6),(5,7),(5,8),(6,10),(7,13)]
# t_dict = {}
# for t in t_list:
#     key = t[0]
#     val = t[1]
#     t_dict[key] = t_dict.get(key,[key])+ [val]
# final_t1 = [tuple(v) for v in t_dict.values()]
# print("T1 Grouped:",final_t1)

test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
result = []

for first,second in test_list:
    found = False
    for i in range(len(result)):
        if result[i][0] == first:
            result[i] = result[i]+(second,)
            found = True
            break
    if not found:
        result.append((first,second))
print(result)

test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
result = []

# for first, second in test_list:
#     found = False
    
#     # Check if we already have a tuple starting with 'first'
#     for i in range(len(result)):
#         if result[i][0] == first:
#             # Tuples are immutable, so we create a new one by adding the new value
#             result[i] = result[i] + (second,)
#             found = True
#             break
            
#     # If no matching initial element was found, start a new tuple
#     if not found:
#         result.append((first, second))

# print(result)
# # Output: [(5, 6, 7, 8), (6, 10), (7, 13)]

# PRACTICE THIS: session5_data_structures.py

print("=== Session 5: Tuples, Sets, Dictionaries ===")

# # ======== TUPLES ========
# print("\n--- Tuple Tasks ---")
# # T1: Join tuples if similar initial element (Using Dicts to group them!)
# t_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
# t_dict = {}
# for t in t_list:
#     key = t[0]
#     val = t[1]
#     # [CONCEPT UNLOCKED: dict.get(key, default)] -> Safe dictionary access
#     t_dict[key] = t_dict.get(key, [key]) + [val]
# final_t1 = [tuple(v) for v in t_dict.values()] # [CONCEPT UNLOCKED: tuple() conversion]
# print("T1 Grouped:", final_t1)

# # T2: Multiply adjacent
# t_orig = (1, 5, 7, 8, 10)
# t_res = []
# for i in range(len(t_orig)):
#     left = t_orig[i-1] * t_orig[i] if i > 0 else 0
#     right = t_orig[i+1] * t_orig[i] if i < len(t_orig)-1 else 0
#     t_res.append(left + right)
# print("T2 Adjacent Mult:", tuple(t_res))

# # T4: Count data types
# mixed_list = [('hi', 'bye'), {'a', 'b'}, ['hi', 'bye']]
# types_dict = {'List': 0, 'Set': 0, 'Tuples': 0}
# for item in mixed_list:
#     # [CONCEPT UNLOCKED: type()] -> Check data type identity
#     if type(item) == list: types_dict['List'] += 1
#     elif type(item) == set: types_dict['Set'] += 1
#     elif type(item) == tuple: types_dict['Tuples'] += 1
# print("T4 Counts:", types_dict)


# # ======== SETS ========
# print("\n--- Set Tasks ---")
# # S1: Common in 3 lists
# ar1, ar2, ar3 = [1,5,10,20], [6,7,20,100], [3,4,20,30]
# # [CONCEPT UNLOCKED: Set Intersection '&']
# common_sets = list(set(ar1) & set(ar2) & set(ar3))
# print("S1 Common:", common_sets)

# # S2: Unique Vowels
# sentence = "hands-on data science"
# vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
# found_vowels = set([char for char in sentence if char in vowels])
# print("S2 Unique Vowels Count:", len(found_vowels))

# # S3: Binary String Check
# bin_str = "010101"
# # If a string only has 0s and 1s, its set of characters will have a length of 2 or less!
# is_binary = len(set(bin_str)) <= 2
# print(f"S3 Is '{bin_str}' binary?", "Yes" if is_binary else "No")

# # S5: Intersection using ONLY list comprehension
# lst1, lst2 = [15, 9, 18], [9, 10, 4, 15]
# intersection = [x for x in lst1 if x in lst2]
# print("S5 Comp Intersection:", intersection)


# # ======== DICTIONARIES ========
# print("\n--- Dictionary Tasks ---")
# # D1: Key with max unique values
# test_dict = {"CampusX": [5, 7, 9, 4, 0], "is": [6, 7, 4, 3, 3]}
# max_key = ""
# max_unique = 0
# for k, v in test_dict.items(): # [CONCEPT UNLOCKED: dict.items()]
#     unique_count = len(set(v))
#     if unique_count > max_unique:
#         max_unique = unique_count
#         max_key = k
# print("D1 Max Unique Key:", max_key)

# # D2: Replace words from lookup dict
# test_str = "CampusX best for DS students."
# repl_dict = {"best": "is the best channel", "DS": "Data-Science"}
# replaced_words = [repl_dict.get(word, word) for word in test_str.split()]
# print("D2 Replaced:", " ".join(replaced_words))

# # D4: List of Tuples to Dict
# tuple_list = [("akash", 10), ("gaurav", 12)]
# dict_res = {k: [v] for k, v in tuple_list}
# print("D4 Tuple to Dict:", dict_res)

# # D5: Sort Dictionary keys and values
# d_unsorted = {'c': [3, 1], 'b': [12, 10], 'a': [19, 4]}
# # Sort the keys, and sort the list values!
# d_sorted = {k: sorted(v) for k, v in sorted(d_unsorted.items())}
# print("D5 Fully Sorted Dict:", d_sorted)

# === SESSION 5: TUPLES, SETS, DICTS ===

# --- TUPLES ---
# T1: Join Tuples (CORRECTED: Pure Tuple/List logic, NO Dictionaries!)
t_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
t_res = []
for t in t_list:
    if len(t_res) == 0:
        t_res.append(t) # Add first tuple
    elif t_res[-1][0] == t[0]:
        # If the first element matches the previous tuple, concatenate the second element!
        # [CONCEPT UNLOCKED: Tuple Concatenation via +]
        t_res[-1] = t_res[-1] + (t[1],) 
    else:
        t_res.append(t)
print("T1 Grouped:", t_res)

# T2: Multiply adjacent
t_orig = (1, 5, 7, 8, 10)
t2_res = []
for i in range(len(t_orig)):
    left = t_orig[i-1] * t_orig[i] if i > 0 else 0
    right = t_orig[i+1] * t_orig[i] if i < len(t_orig)-1 else 0
    t2_res.append(left + right)
print("T2 Adjacent Mult:", tuple(t2_res))

# T3: Check if same
t1, t2 = (1, 2, 3, 0), (0, 1, 2, 3)
print("T3 Same?", t1 == t2)

# T4: Count data types
mixed = [('hi', 'bye'), {'a', 'b'}, ['hi', 'bye']]
print("T4 Counts - Lists:", sum(1 for x in mixed if type(x) == list), 
      "Sets:", sum(1 for x in mixed if type(x) == set), 
      "Tuples:", sum(1 for x in mixed if type(x) == tuple))

# --- SETS ---
# S1: Common elements in 3 lists
ar1, ar2, ar3 = [1,5,10,20], [6,7,20,100], [3,4,20,30]
print("S1 Common:", list(set(ar1) & set(ar2) & set(ar3)))

# S2: Unique Vowels
s_str = "hands-on data science"
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
print("S2 Unique Vowels:", len(set(c for c in s_str if c in vowels)))

# S3: Binary String Check
bin_str = "010101"
print("S3 Is Binary?", set(bin_str) <= {'0', '1'})

# S4: Union of n arrays
arrays = [[1, 2, 4], [5, 1, 3], [9, 5, 7]]
# [CONCEPT UNLOCKED: Unpacking * for sets]
print("S4 Union:", list(set().union(*arrays)))

# S5: Intersection via List Comp
lst1, lst2 = [15, 9, 18], [9, 10, 4]
print("S5 Intersection:", [x for x in lst1 if x in lst2])

# --- DICTIONARIES ---
# D1: Key with max unique values
test_dict = {"CampusX": [5, 7, 7, 7], "is": [6, 7], "Best": [9, 9, 6, 5]}
max_key = max(test_dict, key=lambda k: len(set(test_dict[k])))
print("D1 Max Unique Key:", max_key)

# D2: Replace words
test_str = "CampusX best for DS students."
repl = {"best": "is the best channel", "DS": "Data-Science"}
print("D2 Replaced:", " ".join([repl.get(w, w) for w in test_str.split()]))

# D3: Convert list to list of dicts
t_list = ["DataScience", 3, "is", 8]
k_list = ["name", "id"]
# Iterate by the length of the key list (steps of 2)
d3_res = [{k_list[0]: t_list[i], k_list[1]: t_list[i+1]} for i in range(0, len(t_list), 2)]
print("D3 List of Dicts:", d3_res)

# D4: Tuples to Dict
tups = [("akash", 10), ("gaurav", 12)]
print("D4 Tuple to Dict:", {k: [v] for k, v in tups})

# D5: Sort Keys and Values
d_un = {'c': [3, 1], 'b': [12, 10], 'a': [19, 4]}
print("D5 Sorted:", {k: sorted(v) for k, v in sorted(d_un.items())})
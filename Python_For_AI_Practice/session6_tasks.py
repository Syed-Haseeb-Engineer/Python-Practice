# # PRACTICE THIS: session6_functions.py
# from functools import reduce # Required for reduce() in Python 3+

# print("=== Session 6: Functions (Map, Filter, Reduce) ===")

# # --- P1: Unique Elements List ---
# def get_unique(input_list):
#     # Sets destroy duplicates, list() converts it back
#     return list(set(input_list))

# print("P1:", get_unique([1,2,3,3,3,4,5]))

# # --- P2: Hyphen Sorting ---
# def sort_hyphenated(seq):
#     # [CONCEPT UNLOCKED: sorted(iterable)]
#     words = seq.split('-')
#     return "-".join(sorted(words))

# print("P2:", sort_hyphenated("green-red-yellow-black-white"))

# # --- P3: Upper/Lower Counter ---
# def case_counter(s):
#     upper = sum([1 for c in s if c.isupper()])
#     lower = sum([1 for c in s if c.islower()])
#     print(f"P3: Upper: {upper}, Lower: {lower}")

# case_counter("CampusX is an Online Mentorship Program")

# # --- P4 & P13: Filter Examples ---
# # [CONCEPT UNLOCKED: filter(lambda, iterable)] -> Keeps items where lambda returns True
# sample_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# even_nums = list(filter(lambda x: x % 2 == 0, sample_nums))
# print("P4 Even Filter:", even_nums)

# vowel_filter = list(filter(lambda x: x.lower() in 'aeiou', "Hello World"))
# print("P13 Vowel Filter:", vowel_filter)

# # --- P5: Perfect Number Checker ---
# def is_perfect(n):
#     if n < 1: return False
#     # Find divisors and sum them
#     divisors = [i for i in range(1, (n // 2) + 1) if n % i == 0]
#     return sum(divisors) == n

# print("P5 Is 6 perfect?", is_perfect(6))
# print("P5 Is 28 perfect?", is_perfect(28))

# # --- P6: Concatenate multiple Dicts (*args) ---
# # [CONCEPT UNLOCKED: *args] -> Accepts any number of dictionaries
# def concat_dicts(*args):
#     result = {}
#     for dictionary in args:
#         result.update(dictionary) # [CONCEPT UNLOCKED: dict.update()]
#     return result

# dic1, dic2, dic3 = {1:10, 2:20}, {3:30, 4:40}, {5:50, 6:60}
# print("P6 Dict Concat:", concat_dicts(dic1, dic2, dic3))

# # --- P7: Word with most occurrences ---
# def most_frequent_word(s):
#     words = s.split()
#     # [CONCEPT UNLOCKED: max(iterable, key=func)] -> Uses list.count to find the max
#     top_word = max(words, key=words.count)
#     return f"{top_word} -> {words.count(top_word)}"

# print("P7 Most Freq:", most_frequent_word("hello how are you i am fine thank you"))

# # --- P9: Closest Point using Lambda ---
# def closest_point(coords, query):
#     # Euclidean distance formula via lambda inside the max/min key!
#     dist = lambda p: ((p[0]-query[0])**2 + (p[1]-query[1])**2)**0.5
#     nearest = min(coords, key=dist)
#     return nearest

# print("P9 Closest Point:", closest_point([(1,1), (2,2), (3,3)], (0,0)))

# # --- P11 & P12: Map Examples ---
# # [CONCEPT UNLOCKED: map(lambda, iter1, iter2)] -> Applies math across multiple lists at once!
# l1, l2, l3 = [1,2], [3,4], [5,6]
# added_lists = list(map(lambda x, y, z: x + y + z, l1, l2, l3))
# print("P11 Map Add 3 Lists:", added_lists)

# bases = [1, 2, 3, 4, 5, 6]
# # We use range(len(bases)) to generate the powers/indexes dynamically
# powers = list(map(lambda base, idx: base ** idx, bases, range(len(bases))))
# print("P12 Map Powers:", powers)

# # --- P14: Reduce Example ---
# # [CONCEPT UNLOCKED: reduce(lambda, iterable)] -> Rolls up a list into a single value
# matrix_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # Adding two lists together merges them. Reduce does this sequentially to flatten it!
# flat_1d = reduce(lambda list_a, list_b: list_a + list_b, matrix_2d)
# print("P14 Reduce Flatten:", flat_1d)

# # --- P15: Employee Map/Filter Combo ---
# employees = [
#     {'fname': 'Nitish', 'lname': 'Singh', 'grade': 'skilled'},
#     {'fname': 'Neha', 'lname': 'Singh', 'grade': 'highly-skilled'}
# ]
# # Step 1: Filter keeps only 'highly-skilled'
# # Step 2: Map extracts the fname + lname
# highly_skilled = list(
#     map(lambda emp: emp['fname'] + " " + emp['lname'], 
#         filter(lambda emp: emp['grade'] == 'highly-skilled', employees))
# )
# print("P15 Highly Skilled Output:", highly_skilled)
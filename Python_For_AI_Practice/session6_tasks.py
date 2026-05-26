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

from functools import reduce

# === SESSION 6: FUNCTIONS ===

# P1: Unique List
def get_unique(lst): return list(set(lst))
print("P1:", get_unique([1,2,3,3,4]))

# P2: Hyphen Sort
def sort_hyphen(s): return "-".join(sorted(s.split('-')))
print("P2:", sort_hyphen("green-red-yellow-black-white"))

# P3: Upper/Lower counter
def case_count(s):
    print(f"P3: Upper: {sum(1 for c in s if c.isupper())}, Lower: {sum(1 for c in s if c.islower())}")
case_count("CampusX is Mentorship")

# P4: Even filter
print("P4:", list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])))

# P5: Perfect Number
def is_perfect(n):
    return n == sum(i for i in range(1, n) if n % i == 0)
print("P5 Is 6 perfect?", is_perfect(6))

# P6: Concat Dicts (*args)
def concat_dicts(*args):
    res = {}
    for d in args: res.update(d)
    return res
print("P6:", concat_dicts({1:10}, {2:20}, {3:30}))

# P7: Most Occurrence
def most_freq(s):
    words = s.split()
    top = max(set(words), key=words.count)
    return f"{top} -> {words.count(top)}"
print("P7:", most_freq("hello how are you i am fine thank you"))

# P8: Histogram Bin 10
def histogram(lst):
    # Math trick to find the bin range: (x-1)//10 * 10
    bins = {}
    for n in lst:
        start = ((n-1)//10) * 10 + 1
        end = start + 9
        key = f"{start}-{end}"
        bins[key] = bins.get(key, 0) + 1
    return bins
print("P8 Histogram:", histogram([13,42,15,37,22,39,41,50]))

# P9: Closest Point
def closest(points, query):
    return min(points, key=lambda p: ((p[0]-query[0])**2 + (p[1]-query[1])**2))
print("P9 Closest:", closest([(1,1), (2,2), (3,3)], (0,0)))

# P10: Bag of Words (Built from scratch!)
def bag_of_words(strings):
    # 1. Build the total vocabulary
    vocab = sorted(list(set(" ".join(strings).split())))
    vectors = []
    # 2. Count frequencies for each string
    for s in strings:
        words = s.split()
        vectors.append([words.count(v) for v in vocab])
    return {"vocab": vocab, "vectors": vectors}
print("P10 BoW:", bag_of_words(["data science", "data analytics science"]))

# P11: Add 3 lists with map/lambda
print("P11 Map Add:", list(map(lambda x,y,z: x+y+z, [1,2], [3,4], [5,6])))

# P12: Power to Index
bases = [1, 2, 3, 4, 5, 6]
print("P12 Powers:", list(map(lambda b, i: b**i, bases, range(len(bases)))))

# P13: Filter Vowels
print("P13 Vowels:", list(filter(lambda c: c.lower() in 'aeiou', "Hello World")))

# P14: Reduce 2D to 1D
mat2d = [[1, 2], [3, 4], [5, 6]]
print("P14 Flatten:", reduce(lambda a, b: a + b, mat2d))

# P15: Map/Filter/Reduce Employees
employees = [
    {'fname': 'Nitish', 'lname': 'Singh', 'grade': 'skilled'},
    {'fname': 'Neha', 'lname': 'Singh', 'grade': 'highly-skilled'}
]
# Transcribing and cleaning up the screenshot logic!
highly_skilled = list(
    map(lambda x: x['fname'] + " " + x['lname'], 
        filter(lambda x: x['grade'] == 'highly-skilled', employees))
)
print("P15 Highly Skilled:", highly_skilled)
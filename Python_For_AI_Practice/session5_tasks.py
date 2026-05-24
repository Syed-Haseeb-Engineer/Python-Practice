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

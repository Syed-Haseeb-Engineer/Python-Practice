import sys

#standard way of buidling everything in memory
def standard_number_list(max_num):
    numbers = []
    for i in range(max_num):
        numbers.append(i)
    return numbers


#The Pythonic Generator way (Yields one at a time)
def generator_number_list(max_num):
    for i in range(max_num):
        yield i # Hands the number back, but remembers where it left off!

#Let's compare memory usage for 1 million numbers
list_result = standard_number_list(1000000)
gen_result = generator_number_list(1000000)

print(f"Standard List Memory: {sys.getsizeof(list_result)} bytes")
print(f"Generator Memory: {sys.getsizeof(gen_result)} bytes") # Incredibly Tiny

# How to use a generator? Just loop over it!
print("\nFetching first 3 values from a generator:")
server_ids = generator_number_list(3)
for server_id in server_ids:
    print(f"Provisioned Server ID: {server_id}")
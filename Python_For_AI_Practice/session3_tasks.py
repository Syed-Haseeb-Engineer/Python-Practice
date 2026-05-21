print("\n --- P1: Reverse Number Pattern ---")
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

print("\n--- P4: Pyramid Pattern ---")
for i in range(1,6):
    for j in range(i,0,-1):
        print(j, end = " ")
    print()

print("\n--- P9: Decimal to Binary ---")
decimal_num = int(input("Enter a decimal number: "))
if decimal_num == 0:
    binary_str  = "0"
else:
    binary_str = ""
    temp = decimal_num
    while temp > 0:
        remainder = temp % 2
        binary_str = str(remainder) + binary_str #How it performs the append as string is inmutuable
        temp = temp // 2
print(decimal_num,"in binary is: ",binary_str)    

print("\n --- P11: Acronym Creator ---")
phrase = input("Enter a phrase (e.g., Data Science Mentorship Program):")
words = phrase.split()
print(words)
acronym = ""
for word in words:
    acronym = acronym + word[0].upper()
print("Acronym: ",acronym)

print("\n--- P12: Applied Middle ----")
s1 = input("Enter string s1 (e.g., campusx): ")
s2 = input("Enter string s2 (e.g., data): ")
mid_index = len(s1)//2
result = s1[:mid_index] + s2 + s1[mid_index:]
print("Result:",result)

print("\n--- P13: Lowercase First ---")
mixed_str = input("Enter a mixed case string: ")
lowers = ""
uppers = ""
for char in mixed_str:
    if char.islower():
        lowers = lowers + char
    elif char.isupper():
        uppers = uppers + char
print("Rearranged:", lowers + uppers)

print("\n ---P14: Sum/Average digit in string ")
alpha_num = input("Enter alphanumerical string: ")
total_sum = 0
count = 0
for char in alpha_num:
    if char.isdigit():
        total_sum = total_sum + int(char)
        count += 1
if count > 0:
    average = total_sum/count
    print("Sum: ",total_sum, "Average: ",average)
else:
    print("No digits found in the string.")

sym_str = input("Enter string to check symentry: ")
str_mid = len(sym_str)//2

if len(sym_str) % 2 !=0:
    print("String is odd")
else:
    if sym_str[:str_mid] == sym_str[str_mid:]:
        print("string is symentric")
    else:
        print("string is not symentric")


print("\n --- P17: Reversed String---")
sentence = input("Enter the String: ")
word_list = sentence.split()
reversed = "".join(word_list[::-1])
print("Reversed: ",reversed)

print("\n--- P20: remove Duplicates ---")
str_dup = input("Enter string with duplicate character: ")
str_unique = []
for char in str_dup:
    if char not in str_unique:
        str_unique.append(char)
str_unique2 = ""
for char in str_unique:
    str_unique2 = str_unique2 + char
print(str_unique2)

# #
# # PRACTICE THIS: session3_strict_solutions.py

# print("=== Session 3: Strings and Lists ===")

# # --- P1: Reverse Number Pattern ---
# print("\n--- P1: Reverse Number Pattern ---")
# for i in range(5, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print() # Moves to the next line

# # --- P4: Pyramid Pattern ---
# print("\n--- P4: Pyramid Pattern ---")
# for i in range(1, 6):
#     for j in range(i, 0, -1):
#         print(j, end="")
#     print()

# # --- P9: Decimal to Binary (Without bin() function to practice loops/strings) ---
# print("\n--- P9: Decimal to Binary ---")
# decimal_num = int(input("Enter a decimal number: "))
# if decimal_num == 0:
#     binary_str = "0"
# else:
#     binary_str = ""
#     temp = decimal_num
#     while temp > 0:
#         remainder = temp % 2
#         # Prepend the remainder to the string
#         binary_str = str(remainder) + binary_str 
#         temp = temp // 2
# print(decimal_num, "in binary is:", binary_str)

# # --- P11: Acronym Creator ---
# print("\n--- P11: Acronym Creator ---")
# phrase = input("Enter a phrase (e.g., Data science mentorship program): ")
# words = phrase.split()
# acronym = ""
# for word in words:
#     # Get the first letter, uppercase it, and add it to our string
#     acronym = acronym + word[0].upper()
# print("Acronym:", acronym)

# # --- P12: Append to Middle ---
# print("\n--- P12: Append Middle ---")
# s1 = input("Enter string s1 (e.g., campusx): ")
# s2 = input("Enter string s2 (e.g., data): ")
# mid_index = len(s1) // 2
# # String Slicing! s1[:mid] gets the first half, s1[mid:] gets the second half
# result = s1[:mid_index] + s2 + s1[mid_index:]
# print("Result:", result)

# # --- P13: Lowercase First ---
# print("\n--- P13: Lowercase First ---")
# mixed_str = input("Enter a mixed case string: ")
# lowers = ""
# uppers = ""
# for char in mixed_str:
#     if char.islower():
#         lowers = lowers + char
#     elif char.isupper():
#         uppers = uppers + char
# print("Rearranged:", lowers + uppers)

# # --- P14: Sum/Avg of Digits in String ---
# print("\n--- P14: Sum/Avg of Digits in String ---")
# alpha_str = input("Enter an alphanumeric string: ")
# total_sum = 0
# count = 0
# for char in alpha_str:
#     if char.isdigit():
#         total_sum = total_sum + int(char)
#         count = count + 1

# if count > 0:
#     average = total_sum / count
#     print("Sum:", total_sum, ", Average:", average)
# else:
#     print("No digits found in the string.")

# # --- P16: Symmetrical String ---
# print("\n--- P16: Symmetrical String ---")
# sym_str = input("Enter a string to check for symmetry: ")
# mid = len(sym_str) // 2

# # Check if length is even first
# if len(sym_str) % 2 != 0:
#     print("Not symmetrical (odd length).")
# else:
#     if sym_str[:mid] == sym_str[mid:]:
#         print("The entered string is symmetrical.")
#     else:
#         print("Not symmetrical.")

# # --- P17: Reverse Words ---
# print("\n--- P17: Reverse Words ---")
# sentence = input("Enter a sentence: ")
# words_list = sentence.split()
# # Reverse the list using slicing [::-1], then join it back into a string with spaces
# reversed_sentence = " ".join(words_list[::-1])
# print("Reversed:", reversed_sentence)

# # --- P20: Remove Duplicates (Using only Lists and Strings) ---
# print("\n--- P20: Remove Duplicates ---")
# dup_str = input("Enter a string with duplicates: ")
# unique_chars = []
# for char in dup_str:
#     # If the character is not already in our list, add it
#     if char not in unique_chars:
#         unique_chars.append(char)

# # Join the list of characters back into a final string
# final_unique_str = "".join(unique_chars)
# print("Original:", dup_str)
# print("Unique:", final_unique_str)


# PRACTICE THIS: session3_missing_tasks.py

# print("=== Session 3: Completing the Missing String/List Tasks ===")

# # --- P6: Natural Logarithm Series ---
# # Statement: Calculate the sum of the first 7 terms of the series: 
# # (x-1)/x + (1/2)*((x-1)/x)^2 + (1/3)*((x-1)/x)^3 + ...
# print("\n--- P6: Natural Log Approximation ---")
# x = float(input("Enter value for x: "))

# if x == 0:
#     print("x cannot be zero (Division by Zero).")
# else:
#     total_sum = 0
#     term_base = (x - 1) / x
    
#     for i in range(1, 8): # First 7 terms
#         # Formula: (1/i) * (term_base ^ i)
#         term_value = (1 / i) * (term_base ** i)
#         total_sum = total_sum + term_value
        
#     print(f"The sum of the first 7 terms is: {total_sum}")


# # --- P7: Sum of series (2 + 22 + 222...) ---
# # Concept: We use String multiplication! "2" * 3 = "222"
# print("\n--- P7: Repeating Digit Series ---")
# n_terms = int(input("Enter number of terms: "))
# digit = input("Enter the digit to repeat (e.g., 2): ")

# series_sum = 0
# for i in range(1, n_terms + 1):
#     # String repetition: digit * i. Then cast to integer to do math!
#     term_str = digit * i 
#     series_sum = series_sum + int(term_str)
    
# print(f"Sum of the repeating series is: {series_sum}")


# # --- P15: Palindrome Checker (Algorithmic Approach) ---
# # Concept: Instead of using the slicing trick [::-1], the curriculum asks 
# # us to check it manually by comparing the first letter to the last, second to second-to-last, etc.
# print("\n--- P15: Strict Palindrome Checker ---")
# pal_str = input("Enter a string (e.g., malayalam): ")

# is_palindrome = True
# str_length = len(pal_str)

# # We only need to loop through the first half of the string
# for i in range(str_length // 2):
#     # Compare front character with the corresponding back character
#     if pal_str[i] != pal_str[str_length - 1 - i]:
#         is_palindrome = False
#         break

# if is_palindrome:
#     print(f"'{pal_str}' is a Palindrome.")
# else:
#     print(f"'{pal_str}' is NOT a Palindrome.")


# # --- P18: Uncommon Words from Two Strings ---
# # Statement: A word is uncommon if it appears exactly once in the combined sentences.
# print("\n--- P18: Uncommon Words ---")
# sentence_a = "apple banana mango"
# sentence_b = "banana fruits mango"

# # Split strings into lists of words
# list_a = sentence_a.split()
# list_b = sentence_b.split()

# # Combine lists using the + operator
# combined_list = list_a + list_b
# uncommon_words = []

# for word in combined_list:
#     # [CONCEPT UNLOCKED: list.count()] -> A built-in List method that counts 
#     # how many times an item appears in the list.
#     if combined_list.count(word) == 1:
#         uncommon_words.append(word)

# print(f"Sentence A: {sentence_a}")
# print(f"Sentence B: {sentence_b}")
# print(f"Uncommon Words: {uncommon_words}")


# # --- P19: Word Location Without using .index() or .find() ---
# # Statement: Find the location of a word, but you are FORBIDDEN from using 
# # the built-in search functions. You must build the logic yourself.
# print("\n--- P19: Manual Word Locator ---")
# long_sentence = "We can learn data science through campusx mentorship program"
# target_word = "campusx"

# word_list = long_sentence.split()
# location = -1 # Default if not found

# # [CONCEPT UNLOCKED: len() in range()] -> Loop through the list using numeric indexes
# for i in range(len(word_list)):
#     if word_list[i] == target_word:
#         location = i + 1  # Add 1 because human counting starts at 1, not 0
#         break

# if location != -1:
#     print(f"Location of the word '{target_word}' is {location}.")
# else:
#     print(f"Word '{target_word}' not found.")
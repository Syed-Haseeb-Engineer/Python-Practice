# print("=== Session 2: Operators, If/Else, Loops ===")

# print("\n --- P1: CTC Calculator ---")
# ctc = float(input("Enter your CTC (in Lakhs): "))
# monthly_salary = (ctc * 100000) / 12

# #Deductions
# hra = monthly_salary * 0.10
# da = monthly_salary * 0.05
# pf = monthly_salary * 0.03
# taxable_income_lakhs = ctc

# tax_rate = 0.0
# if taxable_income_lakhs > 20:
#     tax_rate = 0.30
# elif taxable_income_lakhs > 10:
#     tax_rate = 0.20
# elif taxable_income_lakhs > 5:
#     tax_rate = 0.10

# tax_deduction = monthly_salary * tax_rate
# in_hand = monthly_salary - hra - da - pf - tax_deduction
# print("In-hand monthly Salary: Rs.", in_hand)


# print("\n--- P5: Fibonacci Series (10 terms) ---")
# a,b=0,1
# for _ in range(10):
#     print(a,end=" ")
#     temp = a
#     a = b
#     b = temp + b

# print()

# print("\n--- P6: Factorial ---")
# num = int(input("Enter a number to find factorial: "))
# factorial = 1
# if num < 0:
#     print("Factorial does not exist for negative numbers.")
# elif num == 0:
#     print("Factorial of 0 is 1.")
# else:
#     for i in range(1,num + 1):
#         factorial = factorial * i
#     print("Factorial of",num, "is",factorial)

# print("\n--- P7: Reverse Integer ---")
# num_to_reverse = int(input("Enter an Integer to reverse:"))
# reversed_num = 0


# is_negative = False
# if num_to_reverse < 0:
#     is_negative = True
#     num_to_reverse = num_to_reverse * -1

# while num_to_reverse > 0:
#     last_digit = num_to_reverse % 10
#     reversed_num = (reversed_num * 10) + last_digit
#     num_to_reverse = num_to_reverse//10

# #Again converting to negative number
# if is_negative:
#     reversed_num = reversed_num * -1
# print("Reversed number: ", reversed_num)

# print("\n--- P8: Sum 1 to N, Skip % 5, Stop > 300 ---")
# n_limit = int(input("Enter N: "))
# current_num = 1
# total_sum = 0

# while current_num <= n_limit:
#     if current_num % 5!=0:
#         total_sum = total_sum + current_num
    
#     if total_sum > 300:
#         print("Sum exceeded 300. Stopping")
#         if total_sum == 303:
#             print(current_num)
#         break

#     current_num = current_num + 1

# print("Final Sum:", total_sum)


print("\n--- P10. Numbers with all even digits (1000-3000) ---")
#prining all of them is too long we will print just first 5

count = 0
for i in range(1000, 3001):
    temp = i
    all_even = True
    while temp > 0:
        digit = temp % 10
        if digit % 2 !=0:
            all_even = False
            break
        temp = temp // 10

    if all_even:
        print(i,end=" ")
        count = count + 1
        if count == 5:
            print("... (truncated)")
            break
print()
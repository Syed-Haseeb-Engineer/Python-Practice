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

# print("\n --- P2:Triangle or not ---")
# angle1 = int(input("Enter first angle: "))
# angle2 = int(input("Enter second angel: "))
# angle3 = int(input("Enter third angle: "))

# if (angle1 + angle2 + angle3) > 180 and (angle1 > 0 and angle2 > 0 and angle3 > 0):
#     print("Yes, these angles can form a valid triangle.")
# else:
#     print("No, this is an invalid triangle.")

# print("\n ---P3: profit and loss")
# cp = int(input("Enter the cost price: "))
# sp = int(input("Enter the selling price: "))

# if sp > cp:
#     print("Your in profit of",(sp-cp))
# elif cp > sp:
#     print("Your in loss of",(cp-sp))
# else:
#     print("Neither profit Neither loss")

# print(" ---P4: Menu Driven converter ---")
# while True:
#     op = int(input("""
#     How may i help you please enter
#     1.cm to feet
#     2.km to miles
#     3.USD to INR
#     4.exit
#     """))

#     if op == 1:
#         cm = int(input("Enter cm: "))
#         feet = cm * 0.0328084
#         print("{} cm to {} feet".format(cm,feet))
#     elif op == 2:
#         km = int(input("Enter Kilometers: "))
#         miles = km * 0.621371
#         print("{} km to {} miles.".format(km,miles))
#     elif op == 3:
#         USD = int(input("Enter USD: "))
#         INR = USD * 96.69
#         print("{} USD to {} INR.".format(USD,INR))
#     elif op == 4:
#         print("Thank you. Existing ")
#         break
#     else:
#         print("Invalid Option ")


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


# print("\n --- P9: The 7 and 5 Filter ----")
# count = 0 
# for i in range(2000, 3201):
#     if(i % 7 == 0) and (i % 5 == 0):
#         print(i,end=" ")
#         count += 1

#         if count % 15 == 0: 
#             print()
# print("\n")


# print("\n--- P10. Numbers with all even digits (1000-3000) ---")
# #prining all of them is too long we will print just first 5

# count = 0
# for i in range(1000, 3001):
#     temp = i
#     all_even = True
#     while temp > 0:
#         digit = temp % 10
#         if digit % 2 !=0:
#             all_even = False
#             break
#         temp = temp // 10

#     if all_even:
#         print(i,end=" ")
#         count = count + 1
#         if count == 5:
#             print("... (truncated)")
#             break
# print()

# print("\n ---P11: Robot Movement ---")
# print("Enter the number of steps the robot takes in each direction: ")
# steps_up = int(input("UP: "))
# steps_down = int(input("Down: "))
# steps_left = int(input("Left: "))
# steps_right = int(input("Right: "))

# x_position = steps_right - steps_left
# y_position = steps_up - steps_down

# distance = (x_position ** 2 + y_position ** 2) ** 0.5

# print("The robot's distance from the starting point is: ",int(distance))

# print("--- P12: Prime Number Checker ---")
# num = int(input("Enter a number to check if it is prime: "))

# is_prime = True
# if num <= 1:
#     is_prime = False
# else:
#     limit = int(num ** 0.5) + 1

#     for i in range(2,limit):
#         if num % i == 0:
#             is_prime = False
#             break

# if is_prime:
#     print(num, "is a Prime number.")
# else:
#     print(num, "is Not a prime number.")

# print("\n--- P13: Armstrong Numbers in Range ---")
# lower = int(input("Enter lower range:"))
# upper = int(input("Enter upper range:"))

# for num in range(lower, upper + 1):
#     sum_cubes = 0
#     temp = num
#     while temp >0:
#         digit = temp % 10
#         sum_cubes = sum_cubes + (digit ** 3)
#         temp = temp // 10
    
#     if num == sum_cubes:
#         print(num,end=" ")
# print()

# print("\n--- P14: Clock Angle")
# h = int(input("enter Hour (1-12):"))
# m = int(input("Enter Minute (0-59):"))

# if h ==12:
#     h = 0

# hour_angle = (h * 30) + (m * 0.5)
# minute_angle = m * 6

# #Calculate absolute difference without abs() function
# difference = hour_angle - minute_angle
# if difference < 0:
#     difference = difference * -1

# #Find minimum angle
# if difference > 360 - difference:
#     final_angle = 360 - difference
# else:
#     final_angle = difference

# #Floor it by converting to int
# print("Angle:", int(final_angle))

print("\n ---P15: Rectangle Overlap ---")
print("Enter Rectangle 1 (Top-Left and Bottom-Right):")
l1_x = float(input("L1 X: "))
l1_y = float(input("L1 Y: "))
r1_x = float(input("R1 X: "))
r1_y = float(input("R1 y: "))

print("Enter Rectangle 2 (Top-Left Bottom-Right")
l2_x = float(input("L2 X: "))
l2_y = float(input("L2 Y: "))
r2_x = float(input("R2 X: "))
r2_y = float(input("R2 Y:"))

is_left = (r1_x < l2_x) or (r2_x < l1_x)
is_above = (r1_y < l2_y) or (r2_y < l1_y)

if is_above == True and is_left == True:
    print("Rectanlge Not Overlap")
else:
    print("Rectangles Overlap")

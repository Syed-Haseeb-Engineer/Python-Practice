# 1.cm to Feet 
# 2.km to miles
# 3.usd to inr 
# 4.exit

num = int(input("Enter a number"))
n = int(input("""
What Operation u would like to perform?
1.cm to Feet 
2.km to miles
3.usd to inr 
4.exit
"""))

if n == 1:
    feet = num/30
    print("{}cm to {}feet ".format(num,feet))
elif n == 2:
    mile = num/2.5
    print("{}km to {}miles".format(num,mile))
elif n == 3:
    inr = num*95
    print("{}usd to {}inr".format(num,inr))
elif n == 4:
    print("exiting")
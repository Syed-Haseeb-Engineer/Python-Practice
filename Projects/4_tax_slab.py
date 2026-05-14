#WAP that will give you in hand monthly salary after deduction on CTC- HRA(10%), DA(5%), PF(#%) and taxes deduction as below:
#Salar(Lakhs): Tax(%)
#Below 4: 0%
#4 - 8 : 5%
#8 - 12 : 10%
#12 - 16 : 15%
#16 - 20 : 20%
#20 - 24 : 25%
#Above 24 : 30%

CTC = int(input("Enter your CTC"))
HRA = CTC * 0.1
DA = CTC * 0.05
PF = CTC * 0.03
others = HRA + DA + PF
Tax = 0  


if CTC <= 4:
    Tax = CTC * 0
    salary = CTC - HRA - DA - PF - Tax
    print((salary/12)* 100000)
elif CTC > 4 and CTC <=8:
    Tax = (CTC-4) * 0.05
    salary = CTC - HRA - DA - PF - Tax
    print((salary/12)* 100000)
elif CTC > 8 and CTC <=12:
     Tax = ((CTC - 8) * 0.1) + 4 * 0.05
     salary = CTC - HRA - DA - PF - Tax
     print((salary/12)* 100000)
elif CTC > 12 and CTC <=16:
    Tax = ((CTC - 12) * 0.15) + 4 * 0.05 + 4 * 0.1
    salary = CTC - HRA - DA - PF - Tax
    print((salary/12)* 100000)
elif CTC > 16 and CTC <=20:
    Tax = ((CTC - 16) * 0.2) + 4 * 0.05 + 4 * 0.1 + 4 * 0.15
    salary = CTC - HRA - DA - PF - Tax
    print((salary/12)* 100000)
elif CTC > 20 and CTC <=24:
    Tax = ((CTC - 20) * 0.25) + 4 * 0.05 + 4 * 0.1 + 4 * 0.15 + 4 * 0.2
    salary = CTC - HRA - DA - PF - Tax
    print((salary/12)* 100000)
else:
    Tax = ((CTC - 24) * 0.3) + 4 * 0.05 + 4 * 0.1 + 4 * 0.15 + 4 * 0.2 + 4 * 0.25
    salary = CTC - HRA - DA - PF - Tax
    print((salary/12)* 100000)

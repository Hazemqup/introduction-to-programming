scale = input("Enter the temperature scale. C or F:")
number = float(input("Enter number:"))
convertf =(number*9/5)+32
convertc =number-32*(9/5)

if scale == 'C':
    print(convertf,"F")
elif scale == 'F':
    print(convertc,"C")
else:
    print("invalid scale pleaes put C or F")

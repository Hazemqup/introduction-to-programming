num = int(input("Convert Celsius to Fahrenheit, enter number: "))
convert = (num*9/5)+32
print(convert,"F")
 
scale = input("Enter the temperature scale. C for Celsius and F for Fahrenheit: ")
num = int(input("Enter number: "))
convert_f = (num*9/5)+32
convert_c = num-32*(5/9)
if scale == 'c':
    print(convert_f,"F")
else:
    print(convert_c,"C")

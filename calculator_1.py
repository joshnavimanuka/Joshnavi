import math
num1=eval(input("Enter the num:",))
operator=input("Enter the operator:")
num2=eval(input("Enter the num:",))
if operator == '+':
    res1=num1+num2
elif operator == '-' :
    res1=num1-num2
elif operator == '*' :
    res1=num1*num2
elif operator == '/' :
    res1=num1/num2
elif operator == '%' :
    res1=num1%num2
else:
    print("invalid values")

print("res=",res1)

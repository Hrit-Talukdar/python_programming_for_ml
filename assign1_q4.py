import math
a=int(input("Enter the coefficient of x^2: "))
b=int(input("Enter the coefficient of y: "))
c=int(input("Enter the integer: "))
d=math.sqrt((b*b)-(4*a*c))
x=(-b+d)/(2*a)
y=(-b-d)/(2*a)
print("root1: ",x)
print("root2: ",y)
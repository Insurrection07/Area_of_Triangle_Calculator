a = float(input("Enter the first number "))
b = float(input("Enter the second number "))
c = float(input("Enter the third number "))

s = (a + b + c) / 2
area = (s*(s - a) * (s - b) * (s - c))

print('The area of the triangle is : %0.df' %  area)

#Check if a number is positive, negative, or zero
num = 5
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")





#Grade based on marks
marks = 82
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: Fail")




#Check if number is small, medium, or large
n = 45
if n < 10:
    print("Small number")
elif n < 100:
    print("Medium number")
else:
    print("Large number")






#Check temperature level
temp = 35
if temp < 0:
    print("Freezing")
elif temp < 20:
    print("Cold")
elif temp < 30:
    print("Warm")
else:
    print("Hot")





#leap year or not
year = 2024
if (year % 400 == 0):
    print("Leap Year")
elif (year % 100 == 0):
    print("Not a Leap Year")
elif (year % 4 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")





#day of week
day = 4
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid day number")






#Compare two numbers
x = 10
y =20
if x > y:
    print("x is greater")
elif x < y:
    print("y is greater")
else:
    print("Both are equal")






#age group
age = 16
if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior Citizen")





#Simple calculations
a=8
b=4
op = '/'
if op == '+':
    print("Addition:", a + b)
elif op == '-':
    print("Subtraction:", a - b)
elif op == '*':
    print("Multiplication:", a * b)
elif op == '/':
    print("Division:", a / b)
else:
    print("Invalid operator")


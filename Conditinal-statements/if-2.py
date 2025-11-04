#Check if a year is leap year
year = int(input("Enter year: "))
if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")





#Check if number is positive, negative or zero
n = int(input("Enter number: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")



#Check largest of two numbers
a = int(input("Enter first: "))
b = int(input("Enter second: "))
if a > b:
    print("First is larger")
elif b > a:
    print("Second is larger")
else:
    print("Both are equal")




#if person can vote
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")




#Check if number is multiple of 3 or 7
n = int(input("Enter number: "))
if n % 3 == 0 and n % 7 == 0:
    print("Multiple of both 3 and 7")
elif n % 3 == 0:
    print("Multiple of 3 only")
elif n % 7 == 0:
    print("Multiple of 7 only")
else:
    print("Not multiple of 3 or 7")












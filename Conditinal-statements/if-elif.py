#Check if number is even or odd
num = int(input("Enter number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")




#Check if number is divisible by 5 and 11
n = int(input("Enter number: "))
if n % 5 == 0 and n % 11 == 0:
    print("Divisible by both 5 and 11")
elif n % 5 == 0:
    print("Divisible by 5 only")
elif n % 11 == 0:
    print("Divisible by 11 only")
else:
    print("Not divisible by 5 or 11")




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



#Check if character is uppercase, lowercase or digit
ch = input("Enter a character: ")
if ch.isupper():
    print("Uppercase")
elif ch.islower():
    print("Lowercase")
elif ch.isdigit():
    print("Digit")
else:
    print("Special character")

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





#Find smallest of three numbers
a, b, c = map(int, input("Enter three numbers: ").split())
if a <= b and a <= c:
    print("Smallest:", a)
elif b <= a and b <= c:
    print("Smallest:", b)
else:
    print("Smallest:", c)




#Check student pass or fail
marks = int(input("Enter marks: "))
if marks >= 40:
    print("Pass")
else:
    print("Fail")

#Find absolute value
n = int(input("Enter number: "))
if n < 0:
    print("Absolute value:", -n)
else:
    print("Absolute value:", n)




#Check if alphabet is vowel or consonant
ch = input("Enter an alphabet: ").lower()
if ch in ('a', 'e', 'i', 'o', 'u'):
    print("Vowel")
else:
    print("Consonant")



#Check day type (weekday/weekend)
day = input("Enter day: ").lower()
if day in ("saturday", "sunday"):
    print("Weekend")
else:
    print("Weekday")





#Check eligibility for exam (attendance %)
att = float(input("Enter attendance percentage: "))
if att >= 75:
    print("Allowed for exam")
else:
    print("Not allowed")




#Check number range
num = int(input("Enter number: "))
if num < 0:
    print("Negative number")
elif num >= 0 and num <= 50:
    print("Number between 0 and 50")
elif num > 50 and num <= 100:
    print("Number between 51 and 100")
else:
    print("Above 100")



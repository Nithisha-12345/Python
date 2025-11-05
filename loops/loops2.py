#Print only odd numbers from 1 to 25
print("Odd numbers from 1 to 25:")
for i in range(1, 26):
    if i % 2 != 0:
        print(i)

#whileloop
i = 1
print("\nUsing while loop:")
while i <= 25:
    if i % 2 != 0:
        print(i)
    i += 1



#Print squares of numbers from 1 to 10
print("\nSquares from 1 to 10:")
for i in range(1, 11):
    print(i*i)

#whileloop
i = 1
print("\nUsing while loop:")
while i <= 10:
    print(i*i)
    i += 1




#Count how many numbers from 1 to 50 are divisible by 5
count = 0
for i in range(1, 51):
    if i % 5 == 0:
        count += 1
print("\nCount of numbers divisible by 5 (for loop):", count)


#whileloop
i = 1
count = 0
while i <= 50:
    if i % 5 == 0:
        count += 1
    i += 1
print("Count of numbers divisible by 5 (while loop):", count)



#Print each digit of a number
num = input("\nEnter any number: ")
print("Digits (for loop):")
for digit in num:
    print(digit)


#while loop
num = int(num)
print("\nDigits (while loop):")
while num > 0:
    digit = num % 10
    print(digit)
    num //= 10




# 5) Print Pattern
print("\nPattern using for loop:")
for i in range(1, 5):
    print("*" * i)


#whileloop
print("\nPattern using while loop:")
i = 1
while i <= 4:
    print("*" * i)
    i += 1
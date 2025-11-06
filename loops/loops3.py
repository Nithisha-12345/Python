#Sum of digits of a number
num = int(input("Enter a number: "))
temp = num
sum_digits = 0

while temp > 0:
    digit = temp % 10
    sum_digits += digit
    temp //= 10

print("Sum of digits:", sum_digits)



#Reverse a number
num = int(input("\nEnter a number to reverse: "))
temp = num
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

print("Reversed number:", rev)



#Check Palindrome number
num = int(input("\nEnter a number to check palindrome: "))
temp = num
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

if rev == num:
    print(num, "is a Palindrome ✅")
else:
    print(num, "is NOT a Palindrome ❌")




#Factorial of a number
num = int(input("\nEnter a number to find factorial: "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial of", num, "=", fact)




#Fibonacci Series (first 10 numbers)
print("\nFibonacci Series:")
a = 0
b = 1
print(a, b, end=" ")

for i in range(8):
    c = a + b
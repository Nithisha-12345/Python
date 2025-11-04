#Print numbers from 1 to 10
for i in range(1, 11):
    print(i)


#Print even numbers from 2 to 20
for i in range(2, 21, 2):
    print(i)


#Print the sum of first 5 natural numbers
sum = 0
for i in range(1, 6):
    sum += i
print("Sum =", sum)


#Print multiplication table of 5
n = 5
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")


#Print factorial of 5
n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial of", n, "=", fact)
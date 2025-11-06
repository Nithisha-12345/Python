#Print numbers from 1 to 10
for i in range(1, 11):
    print(i)


#Print even numbers from 2 to 20
for i in range(2, 21):
    if i % 2 == 0:
        print(i)


#Print the sum of first 5 natural numbers
sum = 0
for i in range(1, 6):
    sum = sum+i
print(sum)


#Print multiplication table of 5
n = 5
for i in range(1, 11):
    print(n * i)


#Print factorial of 5
n = 5
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print(fact)
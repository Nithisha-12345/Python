
#to check a number is +ve or not
num = 100
if num > 0:
    print("The number is positive")


#check if person is adult
person_age=20
if person_age >= 18:
    print("yes adult")


#check is student passed or not passmark=35
marks=30
if marks>=35:
    print("pass")



#check if temp is high=30
temp=22
if temp >= 30:
    print("high")



#check if  num is multiple of 5
number=3
if number % 5 == 0:   #num divide by 5 nd then % == 0 means when num divide by 2 nd reminder is 0 we use modulus
    print("yes")



#check is a letter is vowel or not
letter="b"
if letter in ["a", "e", "i", "o", "u"] :
    print("vowel")


#check if year greater than 2000
year=2025
if year>2000:
    print("2st century year")



#check if string contain "hello"
string_name="hello world"
if "hello"  in string_name:
    print("hello")



#check if num is negative
num2=-3
if num2 < 0:
    print("Negative num")
else:
    print("ntg")




#check if num1 greater than num2
number11 = 20
number22 = 30
number33 = 20
if number11 > number22 and number11 > number33:
    print("number11 is greater:" , number11)
elif number22 > number11 and number22 > number33:
    print("number22 is greater:" , number22)
else:
    print("number33 is greater:",number33)


#divisible by 3
num4=34
if num4 % 3 == 0:
    print("divisible by 3")

#check if age is 18
age1=24
if age1 == 18:
    print("yes age is equal")


#age==18
age2=18
if age2 == 18:
    print("yes age is equal")


#mutiple by both 2 & 5
num6=10
if num6 % 2 == 0 and num6 % 5 == 0:
    print("multiple of both 2&5")


#check if num is blw 1 to 10
num7=5
if num7 >= 1 and num7 <= 10:
    print("num is blw 1 to 10")



#check if a string starts with "A"   use startswith() method
name="hello"
if name.startswith("A"):
    print("yes start with A")
else:
    print("No")


#start with "A"
name1="App"
if name1.startswith("A"):
    print("yes start with A")
else:
    print("No")



#for string end with "ing"  use endswith() method
name2="welcome"
if name2.endswith("ing"):
    print("yes ends with ing")
else:
    print("No")


#end with "ing"
name3="welcoming"
if name3.endswith("ing"):
    print("yes ends with ing")




#num is 2 digit or not
num8 = 18
if num8 >= 10 and num8 <= 99:
    print("yes 2 digit")



#num is 3 digit or not
num9 = 22
if num9 >= 100 and num8 <= 999:
    print("yes 3 digit")
else:
    print("No")




#to find a num is square of another num
x=2
y=4
if y == x * x:
    print("yes,y is square of x")
else:
    print("No")


#not square
n=2
m=4
if m != n * n:
    print("No,m is  not square of n")
else:
    print("No")





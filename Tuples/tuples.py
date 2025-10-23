#tuple
tuple = ("apple", "banana", "cherry")
print(tuple)


#we can have duplicate means a value can be repeated
tuple1 = ("1", "2", "3", "4", "5","3","4")
print(tuple1)


#Tuple Length ==len()
tuple = ("apple", "banana", "cherry")
print(len(tuple))


#to create tuple with only 1 item
tuple2 = ("bat",)         #use comma(",")
print(type(tuple2))       #o/p data type is tuple



#it will give o/p as string becoz we did not use camma(",")
tuple3 = ("nikki")
print(type(tuple3))


#Tuple can be in  diff data type:
tuple11 = ("hi", "bye", "hello")
tuple22 = (1, 2, 5, 9, 6)
tuple33 = (True, False)
print(type(tuple11))
print(type(tuple22))
print(type(tuple33))


#we also use diff data types in single tuple
tuple44 = ("nikki", 34, True,"pikki")
print(type(tuple44))

#type()
tuple4 = ("bat","ball")
print(type(tuple4))

#Access Tuple Items
tuple5 = ("hi", "hello", "bye")
print(tuple5[1])

#Negative Indexing
tuple6 = ("apple", "banana", "cherry")
print(tuple6[-1])

#Range of Indexes
tuple7 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tuple7[2:5])


#using end index
print(tuple7[:5])


#using starting index
print(tuple7[2:])


#Negative Indexing for both
print(tuple7[-2:-5])


# to Check if Item Exists using "in" keyword
tuple8 = ("ha", "haha", "hehe")
if "apple" in tuple8:
    print("Yes")


#Change Tuple Values
# 1)change tuple to list
# 2)add item to list
# 3)then covert list to tuple


# "+" operator
tuple10 = ("blue", "yellow", "red")
z = ("green",)
tuple10 += z
print(tuple10)


#Remove Items
#Convert the tuple into a list
#remove "mon"
# convert it back into a tuple
"""tuple11 = ("mon", "tue", "wed")
c = list(tuple11)
c.remove("mon")
tuple11 = tuple(c)
print(tuple11)"""


#del keyword
tuple12 = ("honey", "pie", "cutie")
del tuple12
print("tuple12")


#Unpacking a tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


# Using Asterisk "*"

fruits2 = ("app", "bat", "ball", "cat", "dog")

(mango, banana, *orange) = fruits2

print(mango)
print(banana)
print(orange)


# for Loop in a Tuple
tuple13 = ("apple", "banana", "cherry")
for x in tuple13:
    print(x)


#Using the range() and len() functions
tuple14 = ("ant", "sparrow", "rat")
for i in range(len(tuple14)):
    print(tuple14[i])


#While Loop
tuple15 = ("apple", "banana", "cherry")
i = 0
while i < len(tuple15):
    print(tuple15[i])
    i = i + 1

#Join Two Tuples
tuple11 = ("app", "bell" , "cell")
tuple22 = (1, 2, 3)
tuple33 = tuple1 + tuple2
print(tuple3)


#Multiply Tuples
fruits3 = ("where", "how", "who")
tuple17 = fruits3 * 4

print(tuple17)


#Tuple Methods
#Python has two built-in methods
#count() Returns the number of times a specified value occurs
#index() search for specific value nd returns its position
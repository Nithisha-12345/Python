#changing the value of list 
list = ["app", "bat", "cat"]
list[1] = "blackcurrant"
print(list)


#changing value using range
list1 = ["apple", "banana", "cherry", "orange", "kiwi"]
list1[1:3] = ["mango", "watermelon"]
print(list1)


#insert() method
list3 = ["cat", "dog", "monkey"]
list3.insert(2, "donkey")
print(list3)


#append() method
list4 = ["apps", "zepto", "blinkit"]
list4.append("swiggy")
print(list4)

#extend() method
list5 = ["apple", "banana", "cherry"]
list6 = ["mango", "pineapple", "papaya"]
list5.extend(list6)
print(list5)

#extend() method with diff data types
list7 = ["red", "blue", "green"]
tuple = ("black", "white")
list7.extend(tuple)
print(list7)


#remove() method
list8 = ["nikki", "pikki", "uday"]
list8.remove("nikki")
print(list8)


#pop() method remove item at that index
list9 = ["bell", "rings", "bangles"]
list9.pop(1)
print(list9)



#pop() method remove at end default ga
list10 = ["apple", "banana", "cherry"]
list10.pop()
print(list10)

#del keyword also removes the value at index:
list11 = ["moon", "sun", "stars"]
del list11[0]
print(list11)

#Delete the complete list:
del list11

#clear() method
list12 = ["apple", "banana", "cherry"]
list12.clear()
print(list12)


#sort() method
list13 = ["lion", "donkey", "monkey"]
list13.sort()
print(list13)

#numbers
list15 = [10,20,30,40,50]
list15.sort()
print(list15)


#sort() in descending use keyword argument reverse = True
list14 = ["pegion", "parrot", "sparrow"]
list14.sort(reverse = True)
print(list14)

#numbers
list16 = [10,20,30,40,50]
list16.sort(reverse = True)
print(list16)

#sorting is Case sensitive 
list17 = ["brownie", "Darky", "avacado", "Chicken"]
list17.sort()
print(list17)

#reverse() for reverse order of items
list18 = ["hi", "hello","nikki"]
list18.reverse()
print(list18)

#copy()
list19 = ["hi", "hello","bye","nikki"]
newlist=list19.copy()
print(newlist)

#list()
list20 = ["hi", "hello","bye","nikki"]
newlist1=list(list20)
print(newlist1)

# ":" slice operator
list21 = ["hi", "hello","bye","nikki"]
newlist2=list21[:]
print(newlist2)

#Joining 2 Lists
list01 = ["ant", "ball", "c"]
list02 = [1, 2, 3]
list03 = list01 + list02
print(list03)

#using extend()
list011 = ["ant", "ball", "c"]
list022 = [1, 2, 3]
list011.extend(list022)
print(list011)

#append()
list011.append(list022)

"""
list Methods are:
-----------------
1)insert()

2)append()

3)extend()

4)using range[2:4]

5)remove(1)  giving index no. is 1

6)pop(3)  giving index no. is 1

7)using del keyword

8)clear()

9)sort() default ascending or aphabetical

10)key word  reverse=True like sort(reverse=True) for descending

11)sort() is Case-sensitve

12)reverse()

13)copy()

14)list() like this list1=list(list2)

15): operator list2=list1[:]

16)list3=list+list2

17)list1.append(list2)

18)list1.extend(list2)





"""











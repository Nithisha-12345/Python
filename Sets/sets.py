#Sets
set = {"Hi", "hello", "Bye"}
print(set)


#Duplicates Not Allowed
#Sets cannot have two items with the same value.
set1 = {"nikki", "pikki", "uday", "rathan","nikki"}
print(set1)


# True and 1 are considered the same value
set2 = {"apple", "banana", "cherry", True, 1, 2}
print(set2)


#False and 0 are  also same
set3 = {"ant", "bat", "ball", False, 0, 1, 2}
print(set3)


#type()
set4 = {"samsung", "Mi", "redmi"}
print(type(set4))


#len()
set5 = {1,2,3,4,5,6,7,8}
print(len(set5))


#DataTypes
set6 = {"ha", "hehe", "hurry"}
print(type(set6))
set7 = {1, 2, 4, 8, 3}
print(type(set7))
set8 = {True, False, False}
print(type(set8))

#multiple dataTypes
set9 = {"hi", 5, True, 2, "bye"}
print(type(set9))


#Access  tuple Items so we cannot access items in a set using index
#so using for loop we can access it
set11 = {"hut", "building", "roofhouse"}
for x in set11:
    print(x)


#Check if "monkey" is present in the set
set12 = {"pegion", "monkey", "pig"}
print("monkey" in set12)


#Check if "donkey" is not present in the set
set12 = {"pegion", "monkey", "pig"}
print("donkey" not in set12)


#Add one item to a set using the add()
set13 = {"sun", "moon", "stars"}
set13.add("snow")
print(set13)

#To add items from another set into the current set, use the update()
set14 = {"ha", "hehe", "bye"}
set15 = [1,2,3,4,5]
set14.update(set15)
print(set14)


#To remove an item in a set, use the remove(), or the discard()
set16 = {"apple", "banana", "cherry","grapes"}
set16.remove("banana")
print(set16)


#discard()
set17 = {"chokki", "bun", "bisuit"}
set17.discard("bun")
print(set17)

#Remove a random item by using the pop()
set18 = {"venkateshwara", "laxmi", "narsimha","narayana"}
x = set18.pop()
print(x)
print(set18)


#clear()
set19 = {1,2,3}
x = set19.clear()
print(x)
print(set19)


#for loop
set20 = {"app", "ban", "tiktok"}
for x in set20:
    print(x)



#Join set1 and set2
set21 = {"a", "b", "c"}
set22 = {1, 2, 3}
set23 = set21.union(set22)
print(set23)


#or use this "|"to join
set23 = set21 | set22
print(set23)


#Join multiple sets use union()
set31 = {"x", "y", "z"}
set32 = {8,9,10}
set33 = {"rachi", "shruthi"}
set34 = {"shoes", "mike", "nike"}
set24 = set31.union(set32, set33, set34)
print(set24)

#using symbol |
set24 = set31 | set32 | set33 |set34
print(set24)


#difference() will return a new set that will contain only the items from the first set that are not present in the other set.
set33 = set31.difference(set32)
print(set24)


#or use this symbol "-"
set33 = set31 - set32
print(set24)


#symmetric_difference() method will keep only the elements that are NOT present in both sets.same unna elements ni evadu
set25 = {"dog", "lion", "tiger"}
set26 = {"monkey", "cat", "dog"}
set27 = set25.symmetric_difference(set26)
print(set27)

#or use this  ^ operator
set27 = set25 ^ set26
print(set27)


#frozenset is an immutable version of a set

#frozenset()
A = frozenset({"egg", "mutton", "chicken"})
print(A)
print(type(A))
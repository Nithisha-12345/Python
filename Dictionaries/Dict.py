#Dictionary
dict = {
"name": "Nithu",
"age": 20,
"year": 2005
}
print(dict)


#only printing the values
print(dict["name"])


#cannot have duplicates it override ante replace the original value with new value
dict1 = {
"name1": "Nikki",
"age1": 26,
"year": 1996,
"age1": 30
}
print(dict1)


#len()
print(len(dict1))


#Dictionary Items - Data Types
dict2 = {
"brand": "Ford",
"car": False,
"model": 2000,
"colors": ["red", "white", "blue"]
}
print(dict2)


#type()
print(type(dict2))


#dict() Constructor
"""dict3 = dict(name = "nike", age = 22, country = "India")
print(dict3)"""

#Accessing Items
dict4 = {
"brand": "trends",
"itemname": "Tshirt",
"gift": "bro"
}
x = dict4["itemname"]

#or use get() both same

#get()
x = dict4.get("itemname")


#Get Keys
x = dict4.keys()


#add new keys nd values to dict
dress = {
"brand": "max",
"model": "frock",
"looking": "good"
}
a = dress.keys()
print(a) #before changing

dress["color"] = "white"
print(a) #after changing


#values()
a = dress.values()
print(a)


#updating values in dict
makeup = {
"lipstick": "lakme",
"eyeliner": "mabline",
"kajal": "swissbeauty"
}
b = makeup.values()
print(b) #before changing
makeup["lipstick"] = "kay"
print(b) #after changing


#items()
x = makeup.items()
print(b)


#Check if item present using "in" keyword
dict5 = {
"fruit": "apple",
"color": "red",
"bought": "today"
}
if "apple" in dict5:
    print("Yes, 'apple' is one of the keys in the dict5 dictionary")


#Check if  item not  present using " not in" keyword
if "banana" not  in dict5:
    print("Yes, 'banana' is one of the keys  is  not in the dict5 dictionary")


#Change Values
dict6 = {
"wedding": "friend",
"gift": "saree",
"money": 1000
}
dict6["money"] = 2000
print(dict6)


#update()
dict6.update({"money": 3000})
print(dict6)


#Removing Items
#pop()
dict6.pop("money")
print(dict6)


#popitem()
dict6.popitem()
print(dict6)


#del keyword
del dict6["wedding"]
print(dict6)

#del for complete deleting
#del dict6
#print(dict6)


#clear()
dict6.clear()
print(dict6)

#using for loop
dict7 = {
"veg": "carrot",
"curry": "nice",
"cost": 200
}
for x in dict7:
#all key
    print(x)


# all values
print(dict7[x])


#values()
for x in dict7.values():
    print(x)

#keys()
for x in dict7.keys():
    print(x)


#items()
for x,y in dict7.items():
    print(x)


#copy()
    dict8 = dict7.copy()
print(dict8)


#Nested Dictionaries
fam = {
"child1" : {
    "name" : "uday",
    "year" : 2004
},
"child2" : {
    "name" : "nikki",
    "year" : 2007
},
"child3" : {
    "name" : "pikki",
    "year" : 2011
}
}
print(fam)


#or
child1 = {
"name" : "Emil",
"year" : 2004
}
child2 = {
"name" : "Tobias",
"year" : 2007
}
child3 = {
"name" : "Linus",
"year" : 2011
}

family1 = {
"child1" : child1,
"child2" : child2,
"child3" : child3
}
print(family1)
print(family1["child2"]["name"])

#for loop
for a, obj in family1.items():
    print(a)

for b in obj:
    print(b + ':', obj[b])

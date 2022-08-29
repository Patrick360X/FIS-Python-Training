from multiprocessing.sharedctypes import Value


dict1 = {"age" : 32, "name" : "Pradyumna", "dept" : ["cse", "it", "entc"]}

'''
# prints only values

for x in dict1:
    print(dict1[x])

# printing values inside the dictionary
print()
for x in dict1.values():
    print(x)

# printing keys inside the dictionary
print()

for x in dict1.keys():
    print(x)

# printing items inside the dictionary
print()

for x,y in dict1.items():
    print(x, " : ", y)

'''

print(dict1["dept"])

# Different accessing methods

x = dict1["age"]
print(x)

# using get method

x = dict1.get("dept")
print(x)

print()
# dictionary keys

print("Printing the keys only")
x=dict1.keys()
print(x)

print()

# dictionary values

print("Printing the values only")
x=dict1.values()
print(x)

print()

# adding items to dict

print("Adding new item to dict")
dict1["university"] = "SPPU"
print(x)   # Note here the dynamic updation of x
print()

x = dict1.items()
print(x)

# Changing the value 
x = dict1["age"]
print(x)

print("Updated age")
dict1["age"] = 34
x = dict1["age"]
print(x)

print()
'''
# poping out a value from dictionary

x = dict1.pop("university")
print(x)
'''
print(dict1)
'''
# poping out an item from dictionary

x = dict1.popitem()
print(x)
'''


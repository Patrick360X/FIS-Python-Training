# develop a dict2 where every key no should have value as it's square

from this import d


print()
print("Every Key no. should have Value as it's Square")
dict2 = {}

for i in range(5,11):
    dict2[i] = i * i

print(dict2)

# split the dict into 2 seperate lists, 1 with keys and other with values

print()

List1 = dict2.keys()
List2 = dict2.values()

print("List1: " , str(List1))
print("List2: " , str(List2))

# combine List1 and List2 to form a single dictionary Dict3

print()
dict3 = dict(zip(List1, List2))
print("Dict3 : ",dict3)

# Make a star(*) Pyramid of 10 lines

print()

lines = 10
k = 0

for i in range(1, lines+1):
    for space in range (1, (lines-i)+1):
        print(end = " ")
    while k!= (2*i-1):
        print("* ", end="")
        k += 1
    
    k = 0
    print()

# 5.

for i in range(1, 101):
    if i % 7 == 0 or '7' in str(i):
        print("I am Perfect")
    else:
        print(i)

print()
print()


# 6.
a=48
b=20
c=4
d=72
e=81

if(a>b and a>c and a>d and a>e):
    print("\na = ", a, "is the largest number")
elif(b>c and b>d and b>e):
    print("\nb = ", b, "is the largest number")
elif(c>d and c>e):
    print("\nc = ", c, "is the largest number")
elif(d>e):
    print("\nd = ", d, "is the largest number")
else:
    print("\ne = ", e, "is the largest number")

print()
print()

# 7.

list = ['dict', 1, False, 3.5, 'task', 65]
dict4 = {}
for i in list:
    dict4[i] = type(i)
print(dict4)

print()
print()


# 8.

stock = {"Apple" : 20, "Orange" : 10, "Pears" : 5}
rates = {"Apple" : 78, "Orange" : 40.5, "Pears" : 55, "Banana" : 10}
order = {"Apple" : 3, "Orange" : 7, "Pears" : 6, "Pineapple" : 2}

cost = {}

for i in order.keys():
    if i in stock:
        if stock[i] < order[i]:
            order[i] = stock[i]
        cost[i] = rates[i] * order[i]
        stock[i] = stock[i] - order[i]
print("Total order Cost: ",cost)
print("Updated Stock: ", stock)

print()

str1 = "aabbcdcddefee"

dict1 = dict()
for i in str1:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
for i in dict1.keys():
    if(dict1[i] > 2):
        str1 = str1.replace(i,'z')
print(str1)

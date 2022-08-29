# It will automatically eliminate all the duplicate values

set1 = {'Tommy', True, 2, 1.4, 'Timmy', 45, 2}
print(set1)

#print(set1[2]) TypeError: 'set' object is not subscriptable

for x in set1:
    print(x)

print('timmy' in  set1)

#adding an item to set
set1.add('jerry')
print(set1)

# combining 2 sets

set2 = {1, True, 0, False, 'Donald'}
print(set2)
print(len(set2))

set1.update(set2)
print(set1)

set3 = {1,2,3}
set4 = {'a','b','c'}

print(set3.union(set4))

print("Difference")

A1 = {1,2,3,4,5,7,8}
A2 = {2,3,5,6,9,10}

print(A1.difference(A2))

print(A2.difference(A1))
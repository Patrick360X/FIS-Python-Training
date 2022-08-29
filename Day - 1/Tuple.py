tup = (1, "Tommy", 3, 4.9, 5)
print(tup[0])
print(tup)
print()

u = (tup, (1,2,3), (4,6,7))
print(u)
print(u[2])
print()

t = (1, [2,3,4], 3, [5,6,7], 5)

a,b,c,d,e = t

print(b)
print(d)

b,d = d,b

print(b)
print(d)

print(t.count(4))

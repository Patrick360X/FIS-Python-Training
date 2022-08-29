occupation = "engineer"
location = "Bangalore"
info = "I am a {}, my job location is {}."
print(info.format(occupation, location))

print()

name = "tommy timmy"
name1 = name.replace('m','n')
print(name1.strip())

# Reverse a string

place2 = location[::-1]
print(place2)

# String Strip
state = "  madhya pradesh   "
res_st = state.strip( )
print(res_st)

state = "###madhya pradesh "
res_st = state.strip('#')
print(res_st)

#plaindrome

test = input('Enter string: ')
test1 = test[::-1]

if test == test1:
    print('It is a palindrome')
else:
    print("It's not a palindrome")

#upper and lower

occ = occupation.upper()
loc = location.lower()
print(occ)
print(loc)
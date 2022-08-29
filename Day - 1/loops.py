user = input("Enter your location: ")
if user == "Pune":
    print("Happy Ganesh Chaturthi")
elif user == "Bangalore":
    print("My Job location")
else:
    print("Mera Bharat mahan")
print("End of if-else loop")

# count no. of occurances
count = 0
for i in 'tommy timmy':
    if(i == 'm'):
        count += 1

print("Count of character m: " + str(count)) 

# break statement
for x in range(10):
    if x == 5:
        break
    print(x)
else:
    print("Reached till the end of loop")

# continue statement
for x in range(10):
    if x == 5:
        continue
    print(x)
else:
    print("Reached till the end of loop")

# multiples of 9 in between 333 till 666

print("Multiples of 9 in between 333 till 666")

for i in range (333,667):
    if(i % 9 == 0):
        print(i, end=" ")
print()

# Generate first and last prime number in between 1000 and 9000

first = 9000
last = 1000

for i in range(last, first+1):
    flag = True
    for j in range(2,  round(i**0.5)):
        if(i%j == 0):
            flag = False
            break
    if(flag):
        if(i<first):
            first = i
        elif(i>last):
            last = i
print("First Prime no. : "+str(first))
print("Last Prime no. : "+str(last))
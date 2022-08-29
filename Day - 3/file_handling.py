f = open("text.txt",'r')
line = f.read() 
print(line)

print(type(line))
print(len(line))

f.close()
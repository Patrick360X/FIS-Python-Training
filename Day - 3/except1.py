a = 10/0
print(a)
try:
    b = 10/0
except Exception as e:
    print(e)
else: 
    print(b)

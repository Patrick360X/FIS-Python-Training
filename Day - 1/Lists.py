a = [1, "Tommy", 3, 4.9, 5]
print("Length of List: ",len(a))

# Print with Index
print()
print("Print with Index")
for x in range(len(a)):
    print("At index ", x, " ->", a[x])

# Print without index
print()
print("Print without Index")
for b in a:
    print(b)

grades = [54, 76, 34, 76, 88, 23, 51]
print(grades)

grades.append(77)
print(grades)

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]

c = a + b
print(c)
a.extend(b)
print(a)

print(grades.count(76))
print(grades[2])

grades[2] = 98
print(grades[2])

print(a)
a.insert(2, 3445)
print(a)

a.insert(len(a), 587)
print(a)

a.insert(-1, 45)
print(a)
print()

print(grades)
print("Length of list before popping: ", len(grades))
popped = grades.pop(2)
print()

print(grades)
print("Length of list after popping: ", len(grades))
print()

# Unique list items

uniq_grades = list(dict.fromkeys(grades))
print(uniq_grades)
print()

# Removing from list
print(uniq_grades.index(76))

grades.remove(51)
print(grades)
print()

uniq_grades.insert(44,44)
print(uniq_grades)
print()

# Giving value and know it's index in list

print(grades)
print(grades.index(88))
print()

sum_grades = 0
prod_grades = 1
for i in range(0,len(grades)):
    sum_grades = sum_grades + grades[i]
    prod_grades = prod_grades * grades[i]
print("Sum of Grades: ", sum_grades)
print("Product of Grades: ", prod_grades)
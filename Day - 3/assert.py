student_grades = [65,78,51,87,35,92]

i = 0

for i in range(len(student_grades)):
    assert student_grades[i] != 0, "You Failed"
    if student_grades[i] >= 40:
        print("You Passed Exams")
    else:
        print("You need to improve")
print("It is over")


print("STUDENT GRADING SYSTEM")
name = input("Enter student name: ")
marks = []
for i in range(3):
    mark = float(input("Enter mark in Subject " + str(i + 1) + ": "))
    marks.append(mark)
total = sum(marks)
average = total / 3
print("\nSTUDENT RESULT")
print("Student Name:", name)
print("Total Marks:", total)
print("Average Marks:", average)

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
elif average >= 40:
    grade = "E"
else:
    grade = "F"
print("Grade:", grade)
if all(mark >= 35 for mark in marks):
    print("Result: PASS")
else:
    print("Result: FAIL")
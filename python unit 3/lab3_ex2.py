students = {}
n = int(input("Enter number of students: "))
for i in range(n):

    name = input("\nEnter student name: ")

    marks = []

    for j in range(3):

        mark = int(input("Enter subject mark: "))
        marks.append(mark)

    total = sum(marks)

    average = total / 3

    if average >= 90:
        grade = "A+"

    elif average >= 80:
        grade = "A"

    elif average >= 70:
        grade = "B"

    elif average >= 60:
        grade = "C"

    elif average >= 50:
        grade = "D"

    else:
        grade = "F"

    students[name] = {
        "Marks": marks,
        "Total": total,
        "Average": average,
        "Grade": grade
    }
print("\nSTUDENT REPORT")
for name, details in students.items():

    print("\nName:", name)
    print("Marks:", details["Marks"])
    print("Total:", details["Total"])
    print("Average:", details["Average"])
    print("Grade:", details["Grade"])
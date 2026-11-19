with open("students.txt", "w") as file:

    n = int(input("Enter number of students: "))

    for i in range(n):
        name = input("Enter student name: ")
        usn = input("Enter USN: ")
        marks = input("Enter marks: ")

        file.write(name + "," + usn + "," + marks + "\n")

print("\nStudent data saved successfully")

with open("students.txt", "r") as file:
    print("\nStudent Details:")

    for line in file:
        print(line.strip())
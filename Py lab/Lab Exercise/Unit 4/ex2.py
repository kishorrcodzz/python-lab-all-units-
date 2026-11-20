print("STUDENT DATA MANAGER")
file = open("students.txt", "w")
n = int(input("Enter the number of students: "))
for i in range(n):
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    mark = input("Enter student mark: ")
    file.write(name + "," + roll_no + "," + mark + "\n")
file.close()
file = open("students.txt", "r")
print("\nSTUDENT DETAILS")

for line in file:
    data = line.strip().split(",")
    print("Name:", data[0])
    print("Roll Number:", data[1])
    print("Mark:", data[2])
    print("------------------")
file.close()
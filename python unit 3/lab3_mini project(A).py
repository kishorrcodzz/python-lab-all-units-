attendance = {}
n = int(input("Enter number of students: "))
for i in range(n):

    name = input("Enter student name: ")

    status = input("Enter P for Present or A for Absent: ").upper()

    attendance[name] = status

print("\nATTENDANCE REPORT")

for name, status in attendance.items():

    if status == "P":
        print(name, "- Present")

    else:
        print(name, "- Absent")

present = list(attendance.values()).count("P")

absent = list(attendance.values()).count("A")

print("\nTotal Present:", present)
print("Total Absent:", absent)
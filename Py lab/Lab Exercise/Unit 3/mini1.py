print("STUDENT ATTENDANCE TRACKER")
attendance = {}
n = int(input("Enter the number of students: "))
for i in range(n):
    name = input("Enter student name: ")
    status = input("Enter attendance (Present/Absent): ")
    attendance[name] = status
print("\nATTENDANCE REPORT")

for name, status in attendance.items():
    print(name, ":", status)
present = 0
absent = 0

for status in attendance.values():
    if status.lower() == "present":
        present += 1
    else:
        absent += 1
print("\nTotal Present:", present)
print("Total Absent:", absent)
print("Student Details and Calculations")

name = input("Enter student name: ")
roll_no = input("Enter USN number: ")

mark1 = float(input("Enter first subject mark: "))
mark2 = float(input("Enter second subject mark: "))
mark3 = float(input("Enter third subject mark: "))

total = mark1 + mark2 + mark3
average = total / 3

print("\nStudent Details")
print("Name:", name)
print("USN Number:", roll_no)
print("Total Marks:", total)
print("Average Marks:", average)
import csv

with open("payroll.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Employee Name", "Basic Salary", "Bonus", "Total Salary"])

    n = int(input("Enter number of employees: "))

    for i in range(n):
        name = input("Enter employee name: ")
        basic = float(input("Enter basic salary: "))
        bonus = float(input("Enter bonus: "))

        total = basic + bonus

        writer.writerow([name, basic, bonus, total])

print("\nPayroll data saved successfully")

with open("payroll.csv", "r") as file:

    reader = csv.reader(file)

    print("\nPayroll Report:")

    for row in reader:
        print(row)
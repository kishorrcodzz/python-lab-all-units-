import csv
print("PAYROLL MANAGEMENT SYSTEM")
file = open("payroll.csv", "w", newline="")
writer = csv.writer(file)
writer.writerow(["Name", "Basic Salary", "Allowance", "Total Salary"])
n = int(input("Enter the number of employees: "))

for i in range(n):
    name = input("Enter employee name: ")
    basic = float(input("Enter basic salary: "))
    allowance = float(input("Enter allowance: "))
    total = basic + allowance
    writer.writerow([name, basic, allowance, total])
file.close()
file = open("payroll.csv", "r")
reader = csv.reader(file)
print("\nPAYROLL DETAILS")
for row in reader:
    print(row)
file.close()
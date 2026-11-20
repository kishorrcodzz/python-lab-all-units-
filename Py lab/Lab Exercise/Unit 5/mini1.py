import csv
import matplotlib.pyplot as plt
print("RETAIL SALES DASHBOARD")
file = open("sales.csv", "w", newline="")
writer = csv.writer(file)
writer.writerow(["Product", "Sales"])
n = int(input("Enter the number of products: "))
for i in range(n):
    product = input("Enter product name: ")
    sales = float(input("Enter sales amount: "))
    writer.writerow([product, sales])
file.close()
file = open("sales.csv", "r")
reader = csv.reader(file)
next(reader)
products = []
amounts = []
print("\nSALES REPORT")

for row in reader:
    product = row[0]
    amount = float(row[1])
    products.append(product)
    amounts.append(amount)
    print(product, ":", amount)
file.close()
total_sales = sum(amounts)
print("\nTotal Sales:", total_sales)
if len(amounts) > 0:
    print("Highest Sales:", max(amounts))
    print("Lowest Sales:", min(amounts))
    plt.bar(products, amounts)
    plt.title("Retail Sales Dashboard")
    plt.xlabel("Products")
    plt.ylabel("Sales Amount")
    plt.show()
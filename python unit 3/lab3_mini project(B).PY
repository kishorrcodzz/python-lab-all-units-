sales = {}
n = int(input("Enter number of products: "))
for i in range(n):

    product = input("Enter product name: ")

    amount = float(input("Enter sales amount: "))

    sales[product] = amount

print("\nSALES REPORT")

for product, amount in sales.items():

    print(product, ":", amount)

total = sum(sales.values())

print("\nTotal Sales =", total)

if sales:
    highest = max(sales, key=sales.get)

    print("Highest Selling Product:", highest)

    print("Highest Sales Amount:", sales[highest])
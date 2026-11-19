name = input("Enter customer name: ")

item = input("Enter item name: ")

price = float(input("Enter item price: "))

quantity = int(input("Enter quantity: "))

total = price * quantity

gst = total * 0.05

final_amount = total + gst

print("\n------- BILL -------")

print("Customer Name:", name)
print("Item:", item)
print("Price:", price)
print("Quantity:", quantity)
print("Total:", total)
print("GST (5%):", gst)
print("Final Amount:", final_amount)

print("--------------------")
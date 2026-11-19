print("UNIT CONVERTER")
print("1. Kilometres to Miles")
print("2. Celsius to Fahrenheit")
print("3. Kilograms to Pounds")
choice = int(input("Enter your choice: "))
if choice == 1:
    km = float(input("Enter kilometres: "))
    miles = km * 0.621371
    print("Miles =", miles)

elif choice == 2:
    celsius = float(input("Enter Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("Fahrenheit =", fahrenheit)

elif choice == 3:
    kg = float(input("Enter kilograms: "))
    pounds = kg * 2.20462
    print("Pounds =", pounds)

else:
    print("Invalid choice")
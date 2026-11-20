print("Simple Calculator")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Result:", num1 + num2)
elif choice == 2:
    print("Result:", num1 - num2)
elif choice == 3:
    print("Result:", num1 * num2)
elif choice == 4:
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Division by zero is not possible")
else:
    print("Invalid choice")

print("\nArea Calculation")
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
rectangle_area = length * breadth
print("Area of Rectangle:", rectangle_area)
radius = float(input("Enter radius of circle: "))
circle_area = 3.14 * radius * radius
print("Area of Circle:", circle_area)
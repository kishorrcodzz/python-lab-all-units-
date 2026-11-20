num = int(input("Enter a number: "))
n = int(input("Enter a number to find factorial: "))
print("PRIME NUMBER CHECK")
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

print("\nFACTORIAL PROGRAM")
factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i
print("Factorial of", n, "is", factorial)
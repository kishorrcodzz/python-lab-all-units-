import random
while True:
    choice = input("Roll the dice? (y/n): ")

    if choice.lower() == "y":
        number = random.randint(1, 6)
        print("Dice Number:", number)

    elif choice.lower() == "n":
        print("Thank you for playing!")
        break

    else:
        print("Invalid choice")
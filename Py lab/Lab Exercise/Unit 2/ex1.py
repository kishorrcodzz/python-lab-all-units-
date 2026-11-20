import random
print("NUMBER GUESSING GAME")
number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == number:
    print("Congratulations! You guessed correctly.")
elif guess < number:
    print("Your guess is too low.")
    print("The correct number is:", number)
else:
    print("Your guess is too high.")
    print("The correct number is:", number)
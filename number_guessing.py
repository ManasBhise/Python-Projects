# Generate Random Number
import random
x = random.randint(0,10)

# Input number from user and setting count variable to 0
n = int(input("Enter your guess: "))
count = 0

# Conditions
while (n!=x):
    if (n > x):
        print("Number guess is higher than actual number")
        count += 1
        n = int(input("Enter your guess: "))
    else:
        print("Number guess is lower than the actual number")
        count += 1
        n = int(input("Enter your guess: "))

print("You guessed it right congratulations!! and you took", count, "chances")
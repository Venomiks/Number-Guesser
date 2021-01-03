import random

print("Lets guess numbers")
print("Numbers are generated form 1 to 10")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

number = random.choice(numbers)

print(number)

answer = int(input("What is your guess?"))

#state machine
def Answer():
    if answer == random.choice(numbers):
        print(" you win")

Answer()

#hint generator
def Hint():
    if number /2:
        hint = "it's an even digit"
    else:
        hint2 = "It's an uneven digit"
    if answer != random.choice(numbers):
        if number /2:
            print(f"Here's a hint for you: {hint}")
        else:
            print(f"Here's a hint for you: {hint2}")

Hint()
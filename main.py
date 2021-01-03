import random

print("Lets guess numbers")
print("Numbers are generated form 1 to 10")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

number = random.choice(numbers)

#print(number)

answer = int(input("What is your guess?"))

#state machine
def Answer():
    if answer == number:
        print(" you win")

while True:

    print("Try again")

    Answer()

#hint generator
    def Hint():
        if number % 2 == 0:
            hint = "it's an even digit"
        else:
            hint2 = "It's an odd digit"
        if answer != number:
            if number % 2 == 0:
                print(f"Here's a hint for you: {hint}")
            else:
                print(f"Here's a hint for you: {hint2}")

    Hint()

    Answer()
    if answer != number:
        pass
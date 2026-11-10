import random

# super easy way
# target = random.randint(1, 100)

# while True:
#     guess = int(input('Guess the random number between 1 and 100: '))
#     if guess < target:
#         print("too low")
#     elif guess > target:
#         print("too high")
#     elif guess == target:
#         print("congrats, you're right")
#     else:
#         print("not a valid entry")

# proper way that accounts for wrong type of entries
target = random.randint(1, 100)
while True:

    try:
        guess = int(input('Guess the number between 1 and 100: '))

        if guess < target:
            print("too low")
        elif guess > target:
            print("too high")
        else:
            print("congrats, you're right")
            break

    except ValueError:
        print("invalid entry")


import random

while True:
    choice = input('roll the dice y/n: ').lower()
    if choice == 'y':
        print(f"your dice rolled a {random.randint(1, 6)} and {random.randint(1, 6)}")
    elif choice == 'n':
        print("see you next time")
        break
    else:
        print("invalid choice")

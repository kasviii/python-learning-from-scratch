
import random

choices =("r","p","s") #we could have made a list but we chose tuple coz dont want choices to be modified
emojis = {"r": "🪨", "s":"✂️", "p":"📃"}
while True:
    choicee = input("rock paper scissors (r/p/s): ").lower()
    # if choice != "r" and choice != "p" and choice != "s":-->we could do this but instead we declared a choices tuple and therefore wrote an easier code

    if choicee not in choices:
        print("invalid choice!")
        continue
    comp = random.choice(choices)

    #  if choicee =="r":
    #     print("🪨")
    # elif choicee == "s":
    #     print("✂️")
    # else:
    #     print("📃")-->we could do it this way but instead we declared a dict and used that, hence making the code more compact

    print(f"you chose {emojis[choicee]}  and computer chose {emojis[comp]}")

    if choicee == comp:
        print("tie")
    elif (choicee == "r" and comp == "s") or \
    (choicee == "s" and comp =="p") or \
    (choicee == "p" and comp == "r"):
        print("user won")
    # apparently adding a backslash lets the interpreter know that the code continueing in the next like is part of this lines code and so we dont have to write extra long lines of code and hence better readability
    else:
        print("computer won")

    keepgoing = input("continue playing?(y/n): ").lower()
    if keepgoing == "n":
        print("bye loser")
        break
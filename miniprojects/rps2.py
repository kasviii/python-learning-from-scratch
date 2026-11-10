#refactoring = changing structure of code without changing functionality
#modularization= breaking down code into smaller reusable modules

import random

choices =("r","p","s")
emojis = {"r": "🪨", "s":"✂️", "p":"📃"}

def user_choice():
    while True:
        choicee = input("rock paper scissors (r/p/s): ").lower()

        if choicee in choices:
            return choicee
        else:
            print("invalid choice!")

def display_choices(choicee, comp):
    print(f"you chose {emojis[choicee]}  and computer chose {emojis[comp]}")

def winner(choicee, comp):
    if choicee == comp:
        print("tie")
    elif (choicee == "r" and comp == "s") or \
    (choicee == "s" and comp =="p") or \
    (choicee == "p" and comp == "r"):
        print("user won")
    else:
        print("computer won")

def game():
    while True:
        choicee = user_choice()         
        comp = random.choice(choices)
        display_choices(choicee, comp)
        winner(choicee, comp)
        keepgoing = input("continue playing?(y/n): ").lower()
        if keepgoing == "n":
            print("bye loser")
            break

game()
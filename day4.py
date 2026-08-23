#========IF ELSE========##
a = int(input("enter age:"))
if(a>18):
    print("you can legally drive")
else:
    print("you may not drive")
#if accepts condition operatos like <,>,<=,>=,==,!=
print(a>18)
print(a<18)
print(a==18)# and so on, all of these gave true or false as answer which helped if else

#elif example
apple=200
budget=int(input("how much money do you have:"))
if(budget-apple>50):
    print("this is a good purchase")
elif(budget-apple==50):
    print("do you absolutely need this item?")
else:
    print("this purchase is not recommended")

#nested if example
#messy example cos i freehanded whatever but it works
b=int(input("enter b:"))
babe=int(input("enter babe:"))
bebe=int(input("enter bebe:"))
if(b<babe):
    if(b<bebe):
        print("i am the smallest number")
    elif(bebe<b):
        print("bebe is smallest")
    else:
        print("b is not the smallest")
elif(babe<bebe):
    if(babe<b):
        print("i really am the smallest")
    else:
        print("babe is also not the smallest")
else:
    print("bebe=smallest")



import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print("hour:"+timestamp)
timestamp = time.strftime('%M')
print("min:"+timestamp)
timestamp = time.strftime('%S')
print("sec:"+timestamp)

#mini concept project-make a code that greets you good afternoon/evening/morning/night
import time

timestamp = time.strftime('%H:%M:%S')
print(timestamp)

hour = int(time.strftime('%H'))

if hour < 12:
    print("Good morning")

elif hour < 17:
    print("Good afternoon")

elif hour < 22:
    sleeping = input("Are you sleeping? (yes/no): ")
    if sleeping == "yes":
        print("Good night")
    else:
        print("Good evening")

else:
    print("Why are you even up?")



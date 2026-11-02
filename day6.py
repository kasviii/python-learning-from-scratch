#tuple uses ()
tup = (1,45,3)
tupl=(1)
tupll = (1,)#so a tuple with aa single value is treated like int, and therefore we have to leave a comma in parenthesis to define class as tuple
print(type(tup),type(tupll),type(tupl))
#tup[0]=90#will give error as tuples values are immutable
if 45 in tup:
    print(True)

#we can do slicing in tuple
tup2=tup[1:3]#we can do the other ways to :3, 1: , 1:8:3(remember third value is jump by this one)
print(tup2)

#tuple methods: we can manipulate tuples but not directly, we first convert them into list, do our operation and then convert back
countries=("spain","venice","italy","england","brisbane")
temp = list(countries)
temp.append("russia")
temp.pop(3)
temp[2] = "switzerland"
countries = tuple(temp)
print(countries)
#we can concatenate two tuples without converting them to list
seen = ("leh","ladakh","andaman")
vacay=countries+seen
print(vacay, type(vacay))

#methods
tutu = (1,2,4,3,1,2,4,6,2,3,4,5,7)
res = tutu.count(2)
print(res)#tuple.count(element)
res = tutu.index(4)#index() gives index of first occurance of element specified
sir = tutu.index(4,3,7)# we can specify brackets in which we want searching => tuple.index(element, start, end)
print(res, sir)
print(len(tutu))

###kon banega crorepati program


questions = [
    "What is the capital of India?",
    "Who is known as the Father of the Nation?",
    "Which planet is known as the Red Planet?",
    "How many days are there in a week?",
    "Which is the largest ocean?"
]

answers = ["Delhi", "mothers", "Mars", "7", "Pacific"]

play = input("Would you like to play KBC? ")

prize = 0
question = 0

if play.lower() == "yes":

    while question < len(questions):
        print(questions[question])
        answer = input("Your answer: ")

        if answer.lower() == answers[question].lower():
            prize += 1000
            question += 1
            print("Correct! You won:", prize)

        else:
            print("Wrong answer! Game over.")
            break

    print("Your total winnings:", prize)

else:
    print("Maybe next time!")



##docstrings in python
#this is what we did before fstring
letter = "Hey my name is {} and i am from {}"
country = "India"
name = "edison"
print(letter.format(country, name))#gives wrong answer, coz we messed up
print(letter.format(name, country))#this is the answer we want
letter = "Hey my name is {1} and i am from {0}"
country = "India"
name = "edison"
print(letter.format(country, name))#gives right answer coz we specified index wise

print(f"hey my name is {name} and i am from {country}")

txt = "for only {price:.2f} dollars"#.2f means we want till two decimal places
print(txt.format(price = 49))
price = 49.0999
print(f"for only {price:.2f} dollars")
print(f"{2*40}")
print(type(f"{2*40}"))
#if we want to see curly bracket part without values:
print(f"{{2*40}}")


#docstrings= string literals that appear after definition of a function, method, class or module
def square(n):
    '''Takes in a number n, returns its square'''
    print(n**2)
    #'''Takes in a number n, returns its square'''--> this is not a docstring, this wont print as doc string either coz docstring is the like right after def function
square(5)
print(square.__doc__)#unlike comments docstrings can be printed and are not ignored, instead given special treatment

#PEP 8 = python enhancement proposal
#import this in terminal, for python give zen of python, which is like an easter egg, a bunch of rules in python that would work better in a poem ish way

#RECURSION- defining something in terms of itself

def facto(x):
    if x == 1 or x == 0:
        return 1
    else:
        return x*facto(x-1)

print(facto(4))

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
print(fibo(9))

#sets in python= unordered collection of data items, they store multiple items in a single variable in {}
#sets are unchangeable and do not contain duplicate items
s = {2,2,3,4,6, "Car", 5.9, False}
print(s)

m = {}
print(type(m))#this gives dict not empty set

n = set()
print(type(n))#now its empty set

for value in s:
    print(value)

#set methods = 1)joining sets using setname.union(othersetname)
p ={"tiger", 99}
newset = s.union(p)
print(newset)
print(s,p)
#in union the sets were unchanges, a new set got the joint version
#2)we joined sets using setname.update(2ndsetname) this add p to s while p remains the same as before 
print(s.update(p))
print(s, p)
#3)intersection and intersection_update prints items similar to both the sets and former makes a new set while the later updates the existing set from another
cities = {"tokyo", "madrid","seoul"}
cities2 = {"tokyo", "seoul", "berlin"}
cities3 = cities.intersection(cities2)
print(cities3, cities2, cities)
cities.intersection_update(cities2)
print(cities, cities2)
#4)symmetric_difference() and symmetric_difference_update()-> only prints items that are not similar to both the sets
city = {"tokyo", "madrid","seoul"}
cityy = {"tokyo", "seoul", "berlin"}
city3 = city.symmetric_difference(cityy)
print(city3, cityy, city)
cityy.symmetric_difference_update(city)
print(city, cityy)
#5)difference() and difference_update()-> prints items that are only present in original set and not in both
a = {2,3,4}
b = {3,45,6}
c = a.difference(b)
print(c,a,b)
a.difference_update(b)
print(a,b)
#6)isdisjoint()->checks if items in given set are present in another set
e={1,2,4,5,7}
f={4,5,67,2,34}
print(e.isdisjoint(f))
#7)issuperset()-> checks if all the items of a particular set are present in the original set
g={2,4,7}
print(g.isdisjoint(b))
print(e.issuperset(g))
#8)issubset()-> if all items of original set are present in particular set
print(g.issubset(e))

#9)add, update, remove, discard
cities.add("delhi")
print(cities)
s.update(p)
print(s)
cities.remove("tokyo")
print(cities)
#difference between remove and discard is that if we try to delete an item which is not present in set then remove raises an error, whereas discard doesnt
#cities.remove("mumbai")-> gave error
cities.discard("mumbai")
#10)pop()-removes last item of the set but we dont know which item, as sets are unordered
#we can access popped item if we assigne it to a variable
z = {1,2,3,4}
item = z.pop()
print(z)
print(item)
#11)del = deletes the entire set||||| clear = clear items in set and gives empty set
del cities2
# print(cities2)-> gives error coz set deleted
cities.clear()
print(cities)

if 3 in z:
    print("im here")
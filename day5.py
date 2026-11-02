""" Match case statements = looks like a traditional switch-case statement found in other languages, it goes far beyond simple value matching
 by allowing you to destruct, unpack, and verify the shape of your data"""
# x = int(input("enter the value of x: "))
# match x:
#     case 0:
#         print("x is 0")
#     case 4:
#         print("case is 4")
# #unlike switch match has no break
# #this can also use if else
#     case _ if x!=90:
#         print(x, "is not 90")
# #suppose i entered x = 60 then it matches this case and therefore will execute this and leave the function
#     case _ if x!=80:
#         print(x, "is not 80")
#     case _ :
#         print(x)
#     #this default case only executes when the rest do not satisfy

##loops- for and while
# for k in range(4):
#     print(k+1)
# colors = ["pink","red"]
# for color in colors:
#     print(color)
# for i in range(2, 4):
#     print(i)
# for k in range(1, 12, 4):#every fourth number between 1 to 12
#     print(k)

# i = int(input("enter i:"))
# while(i<4):
#     print(i)
#     i+=1
# #else can be used with while loop
# else:
#     print("number is too big")
# #other languages have do while loop, so we do one  the "do" part at least once and then while based on whether the condition has been satisfied

# #emulate do while
# while True:
#     number = int(input("enter a positive number: "))
#     print(number)
#     if not number > 8:
#         break

#break- terminates the loop
for i in range(12):
    print("5x", i+1,"=",5*(i+1))
    if (i+1) == 10:
        break

for i in range(1,101,11):
    print(i,end=" ")
    if i>50:
        break
    else:
        print("eggs")
print("enough")
#continue = leave the iteration
for i in range(12):
    if((i+1)==10):
        print("skip the iteration")
        continue
    print("5x", i+1,"=",5*(i+1))

for i in range(10):
    if(i%2!=0):
        continue
    print(i)

#function= block of code that performs a specific task
#type 1)built in functions:these are precode in python like min(), max(), sum()
a=[1,2,23,4,5]
print(sum(a))

#2)user defined function
def leetcodesolver():
    pass#this is a function, but nothing in it

def dog(dname):
    print("sit",dname)
dog("swiper")

#a function has four type of arguements, default, keyword, variable length and required
#default arg
def name(n="joe", p="Joan", r=str):
    print(f"hi im {n} and this is {p}, r u {r}")
name(r="Clara")#the variable with no deafult value is assigned smthing
name(n="Clara", r="Joe")#this overwrites the default value
name("Clara")#just assigns this to the first variable, regardless of whether it has a default value
name("Amy", "Belle","Judas")
name(r="Ari",p="Kacey")#this is keyword arguement, with key=value, this way interpreter recognizes arg by parameter and order doesnt matter

def avg(a,b,c=2):
    print((a+b)/2)
#avg(b=2)#here a is a required arg so we will get an error

#variable length arg = put *
def average(*num):
    print(type(num))
    sum = 0
    for i in num:
        sum = sum + i
    print("avg is:", sum/len(num))
average(5,6,7,3)
average(5,6,)
#* made num a tuple for we can put as many entries as we like
# similarly ** makes it a dictionary
def name(**name):
    print(type(name))
    print("Hello",name["fname"],name["lname"])
name(lname="Barnes",fname="Troy")

#return statement is used to return the value of the expression back to the calling function
def name(fname,mname,lname):
    return "Hello" +  " " +fname +" "+ mname +" "+lname
print(name("Ace","D","Portgas"))

#list=[], can be changed but tuples cant
marks = [9,34,2,3,54]
#       -5,-4,-3,-2,-1
print(marks[-3])
print(marks[5-3])
print(marks[len(marks)-3])
print(marks[2])

if "ha" in "harry":
    print("yes")

print(marks[2:4])#slicing
print(marks[1:5:2])
#list comprehensions are used for creating new lists from other iterables like lists, tuples, and even in arrays and strings
#syntax=list= expression(item) for iten in iterable if condition
names=["milo","niya","centaur","medusa"]
nameswith_e = [item for item in names if "e" in item]
print(nameswith_e)
#eg 2
nums = [i*i for i in range(10)]
print(nums)
nums = [i*i for i in range(10) if i%2==0]
print(nums)
#list methods
l = [34,5462,12,35,77,54,2,56]
print(l)
print(l.reverse())#will give none as output but it does modify the list
print(l)
print(l.sort())#will give none
print(l)
print(l.sort(reverse=True))#will give none 
print(l)
print(sorted(l))#output is sorted but list has not been affected
print(l)
print(list(reversed(l)))#output is reversed but list is unaffected
print(l)
#print(l.index(1))#gives index of where value is, and this doesnt exist so gives error
print(l.index(12))
print(l.count(12))
m=l.copy() #makes a copy of the list
print(m)
l.append(23)
print(l)
l.insert(2, 234)#insert 234 at index 2
print(l)
m=[23,43,56,67,89]
l.extend(m)
print(l)#modified list l by extending it
k= l+m#if we dont want to modify, we can make a new list and give it values
print(k)

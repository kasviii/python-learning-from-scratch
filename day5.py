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








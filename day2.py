#####15 minute python random recap since i took a break#####
import math
print(math.cos(3.455))##we import math to use certain math functions liek cos or floor

str1 = "today i went for tcs exam."
print(str1)#this prints the string
print(str1.capitalize())#this capitalizes the first word
print(str1.find("went"))#finds the index where the given string exists
print(str1.upper())#capitalizes everything, conversely lower would give small letters
print(type(str1))#tells the datatype

##lists-> they have square brackets and mutable
items = ["harry", 1, 2]
print(items)
items[1] = "lola"
print (items)
list1=[1,2,3,4,5,5]
print(list1)#gives the entire list
s1=set(list1)
print(s1)#prints list without repeated components
#basically we can change the things within a list
##tuple->normal brackets
tup1=(1,2,3)
print(tup1)
#tup1[1]=34 -> if we try to print this, it will give an error as tuples can not be changed(unmutable)
##dictionary-> has curly brackets
dict1 ={"virat": 100,"sachin":200}
print(dict1)
print(dict1.get("sachin"))#will give 200 as thats the assigned value
print(dict1.keys())#gives the key values like virat and sachin
print(dict1.items())#lists everything in the dictionary

#operators
var = int(input())#takes an int input
print(var+77)#performs an operation



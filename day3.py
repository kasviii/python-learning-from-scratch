#######-----STRING METHODS-------######

#strings are immutable
a= "!!!Harry !!!! Harry"
#lets test different methods
print(len(a))
print(a.upper())#upper() method doesnt convert existing string to uppercase coz strings are immutable, it makes a new string altogether
print(a.lower())
print(a.rstrip("!"))#strips the trailing specified character, not leading ones
print(a.replace("Harry","Jojo"))#replaces all instances of harry with jojo
print(a.split(" "))#we split the given string into a list of items separation based by space
heading = "into tHE dark"
print(heading.capitalize())#captializes the first letter and lowercase the rest

#the center() method aligns the string to the center as per teh given parameter
str1= "welcome!!!!"
print(str1)
print(str1.center(50))#so the word welcome got spaces added to it such taht its length is now 50
print(len(str1.center(50)))
print(a.count("Harry"))#counts the number of times the thing is there
print(str1.endswith("!!"))#endswith() is a boolean datatype that tells us what we have asked is true or not
print(str1.endswith("e!",6,8))#it can be used to get specific characters too by specifying start and end index

#startswith() can tell us if the string starts with a given value

#find() searches for the first occurance of the given value and returns its index,
#if value is absent from string thr -1 is returned
str = "he is dan. he is a very weird man"
print(str1.find("is"))
print(str.find("is"))

#index() searches for the first occurance and returns the index where is it, if absent then it raises an exception
#print(str1.index("is"))

#isalnum() returns true only if the entire string has only A-Z, a-z, 0-9
print(str.isalnum())
#isalpha() only true if alphabets 
print(str.isalpha())
#islower()/isupper() returns true if all char as lower/upper case
#isprintable() itrue if all values in the string are printable
print(str.isprintable())#this will turn false if suppose the string has \n

#isspace() returns true of string has white spaces(made with tab or space bar) only
#istitle() true is every words first letter is capital

print(str1.swapcase()) #swaps upper/lower case to lower/upper case
print(str.title())#capitalizes every first letter

#tuple uses ()
tup = (1,45,3)
tupl=(1)
tupll = (1,)#so a tuple with aa single value is treated like int, and therefore we have to leave a comma in parenthesis to define class as tuple
print(type(tup),type(tupll),type(tupl))
#tup[0]=90#will give error as tuples values are immutable

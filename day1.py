"""
=========================================
DAY 1 - PYTHON BASICS
=========================================

Topics Covered:
1. Comments
2. Variables
3. Printing Output
4. Escape Characters
5. Data Types
6. Arithmetic Operators
7. Type Casting
8. User Input
9. Simple Calculator Assignment
"""

# =========================================
# 1. COMMENTS
# =========================================

# Single-line comment

"""
Multi-line comment / docstring

Python allows triple quotes for
multi-line text.
"""
'''
  it also accepts single quotes
'''

# =========================================
# 2. VARIABLES
# =========================================

hi = "how are you"     # Strings need quotes
age = 23              # Integers do not

# print(hi)

# =========================================
# 3. PRINT FUNCTION
# =========================================

print(8 + 9)
print(hi)#will print whats inside the variable hi that we wrote before
print("hi")#will print hi
print("im happy")

# New line character
print("hi\nim happy")

# Printing quotation marks using \"
print("\"hey\"hey")

# sep = separator between values, in this example it separated using ~ but we can use something else too
# end = what gets printed at the end
print(hi, 6, 7, sep="~", end="009\n")

# =========================================
# 4. STRING OPERATIONS
# =========================================

hey = "im kara"
# Concatenation
print(hi + hey)

# Cannot add different data types directly
h = 23
print(hi + h)   # Error

# =========================================
# 5. DATA TYPES
# =========================================

"""
Common Built-in Data Types:

str      -> String
int      -> Integer
float    -> Decimal number
complex  -> Complex number(written as x=complex(8,2) this will give 8+2i)
bool     -> True / False
list     -> Mutable collection(sequenced data)
tuple    -> Immutable collection(sequenced data)
dict     -> Key-value pairs(mapped data)
"""
print(type(hi))#gives the datatype of hi

# Complex number
x = complex(8, 2)
print(x)

# =========================================
# 6. LISTS, TUPLES, DICTIONARIES
# =========================================

# List (mutable)(can be modified)

list1 = [
    8,
    2.3,
    [-4, 5],
    ["apple", "banana"]
]
print(list1)
#lisrs can have int, float, another list

# Tuple (immutable)(can not be modified)

tuple1 = (("parrot", "sparrow"), 1, 2)
print(tuple1)

# Dictionary

dict1 = {"name": "elle"}
print(dict1)

# =========================================
# 7. ARITHMETIC OPERATORS
# =========================================

print(5 + 6)    # Addition
print(5 - 6)    # Subtraction
print(5 * 6)    # Multiplication
print(5 / 6)    # Division
print(5 // 6)   # Floor Division(only gives value before decimal
print(5 % 6)    # Modulus (remainder)
print(5 ** 6)   # Exponent

# =========================================
# 8. TYPE CASTING
# =========================================

"""
Type Casting = converting one data type
to another.

Types:
1. Explicit Type Casting
2. Implicit Type Casting
"""

# Explicit Type Casting

a = "1"
b = "2"

print(a + b)                # 12
print(int(a) + int(b))      # 3

# Implicit Type Casting-python on its own converts the data type because one is of a high order and another of a lower order, the smaller data type gets converted into higher automatically by the interpreter

c = 1.9
d = 8
total = c + d#the answer is in float form due to implicit typecasting
print(total)
print(type(total))

# =========================================
# 9. USER INPUT
# =========================================

name = input("Enter your name: ")
print("My name is", name)
x = input("Enter number: ")
y = input("Enter number: ")
print(x + y)                # Concatenates as it registers the input as a string
print(int(x) + int(y))      # Numerical addition

# =========================================
# 10. ASSIGNMENT - SIMPLE CALCULATOR
# =========================================

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Exponent:", x ** y)
print("Floor Division:", x // y)
print("Modulus:", x % y)

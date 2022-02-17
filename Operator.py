"""
Operator in Python

Arithmetic Operators
Comparison (Relational) Operators
Assignment Operators
Logical Operators
Bitwise Operators
Membership Operators
Identity Operators

"""

###Arithmatic Operator###

from math import ceil, floor
from chemicals import Ceiling


a = 10
b = 15

print("Addition-> ", a+b)
print("Substration-> ", a-b)
print("Miultiple->", a*b)
print("Division->", a/b)
print("Floor Division->", a//b)
print("Modulus->", a % b)
b = 3
print("Exponential->", a**b)


c = a//b
d = floor(a/b)

print(c, d)
print()
###Comprison (Relational) Operators###

a = 10
b = 20

print("Equal to->", a == b)  # False
print("Not Equal to->", a != b)  # True
print("Greater than->", a > b)  # False
print("Less than->", a < b)  # True
print("Grreater than equal to->", a >= b)  # false a>b or a==b
print("Less than equal to->", a <= b)  # False  a<b or a==b
print()
###logical Operator###

t = True
f = False

print("AND ->", f and f)  # f
print("OR ->", f or t)  # t
print("Not->", not f)  # t
print()

###Assignment Operators###

a = 5
print("Equal to ->", a)  # 5
a += 5
print("Addition-> ", a)  # a = a+5 -> a+=5 = 10
a -= 5
print("Substration-> ", a)  # 5
a *= 5
print("Miultiple->", a)  # 25
a /= 5
print("Division->", a)  # 5
a //= 5
print("Floor Division->", a)  # 1.0
a %= 5
print("Modulus->", a)  # 1.0
a **= 5
print("Exponential->", a)  # 1.0

###Bitwise Operators###

print()
###Membership Operators###
s = "Johnathan"

print(("In ->"), ('J' in s))  # ("In->") => In ->, ("J" in s) => True - True
print("Not in ->", "J" not in s)

print()
###Identity Operators###

a = 5
b = 5

print(id(a) == id(b))
print("IS->", a is b)  # True
print("is not->", a is not b)  # False

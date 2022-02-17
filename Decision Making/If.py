"""
Decision Making

If statements

Syntax:

#if statement
if expression:
    block of code

#if else
if expression:
    block of code
else:
    block of code

# if else ladder
if expression:
    block of code
elif expression:
    block of code
else:
    block of code


# nested if else
if expression:
    if expression:
        block of code
    else:
        block of code
else:
    block of code

"""
# if statement
if 10 < 20:
    print("10 is less than 20")

# if else
if 10 > 20:                         # if the expression is true then if block will be executed
    print("10 is less than 20")
else:                               # if the expression is false then else block will be executed
    print("20 is greater than 10")


"""
0 - 49 = Fail(F)
50 - 59 = Pass(P)
60 - 74 = Credit(C)
75 - 84 = Distengtion(D)
85 - 100 = Higher Distingsion(HD)

"""

# if else ladder
mark = 76

if mark <= 49:
    print("F")
elif mark <= 59:
    print("P")
elif mark <= 74:
    print("C")
elif mark <= 84:
    print("D")
elif mark <= 100:
    print("HD")
else:
    pass


# nested if else
gender = "female"
age = 33

if gender == "Male":
    if age < 30:
        print("Eligible")
    else:
        print("not eligible because of age")
else:
    print("not eligible because of gender")


"""
Rock paper sicers

2 players
3 players

P1 = R/P/S
P2 = R/P/S
"""

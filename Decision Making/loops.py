"""
Loops

Loop is a block of code that repeated multiple times.

there are two types of loops in Python - for and while

while expression:
    code

for interator in sequence:
    code
"""

i = 0

while i < 5:
    print(i)
    i = i + 1


"""
i = 0  => i<5 =>  True => 0 => 1
i = 1  => i<5  => True => 1 => 2
i = 2  => i<5  => True => 2 => 3
i = 3  => i<5  => True => 3 => 4
i = 4  => i<5  => True => 4 => 5
i = 5  => i<5  => False...
"""
print("For Loop\n")

st = "Thank you!"

for i in st:
    print(i)

"""
1st iteration -> i = T
2n iteration -> i = h
3rd iteration -> i = a
4th iteration -> i = n
5th iteration -> i = k
6th iteration -> i = 
7th iteration -> i = y
8th iteration -> i = o
9th iteration -> i = u
10th iteration -> i = !
"""

print()
# range will create a sequence of 1-4,
# range() has two arguments,
# 1st is default to 0,
# at least argument is compulsory
# arugemts to range are only numbers

for j in range(15, -10, -1):
    print(j)


# break - loop will terminate the loop on the spot

print()

for i in range(1, 6):
    if(i == 4):
        continue  # continue will terminate the current iteration and next iteration of the loop will be executed
    print(i)


"""
1
2
3
4S
5
"""

print()

st = "Thank you!"
# output -
# T
# h
# a
# n
# k

# hint- use indexing and loop with range

for i in st:
    print(i)

for i in range(0, len(st)):
    print(st[i])

# range(0,10)
#   i = 0   st[i] -> st[0]
#   i = 1   st[i] -> st[1]
#   i = 2   st[i] -> st[2]

print()


"""
using loops print the following:

5

1
12
123
1234
12345

#hint -> to print on the same line you have to search on google.
"""

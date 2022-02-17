"""
String

String is a datatype in python.
It can store any number of characters init gieven that all the characters are in '' or "".
In python we can create multiline string using """""" or '''string'''. 
In multiline string, whitespaces are maintained.

String slicing:

index starts from 0   - left to right
negative  index starts from -1 - right to left

syntax:
variable[start_index:end_index+1]

always start_index < end_index, given that both the index have same sign
"""

st = "I am learning Python3"
#     0123456789
print(st)

print(type(st))

print(st[2])  # char at index 0 from the st will be printed

l = len(st)  # function that returns length

print(l)

print(st[20])

print(st[len(st)-1])  # -> print(st[21 - 1]) -> print(st[20]) -> 3

print(st[-1])

print(st[-2])

st2 = 'John'
#      0123 = index
#     -4-3-2-1 = index
print(st2[len(st2)-1])

# string Slicing
print(st[5:13])

print(st[14:21])

print(st[-21:-23])  # start_index < end_index = false

print(st[-21:-18+1])

# leaning python3
print(st[4:21])

a = st[4:-1]
print(a)

print(st[4:])

print(st[:4])

print(st[:])

# string methods

print(dir(st))

print(st[2:9].index('e'))  # "I am learning Python3", st[2:9] => am lear
# print(st.index.__doc__)

print(st)

print(st.isnumeric())
print(st.isalpha())
print(st.isalnum())

print(st.replace("3", "4"))

print(st.isspace())

print(st.upper())
print(st)


st3 = """This is single line string
    john is a good boy
        he is studying well!!"""

st0 = "This is single line string\n\tjohn is a good boy\n\t\the is studying well!!"
print(st3)
print(st0)


uk = "united kingdom"
print(uk.capitalize())

asc = "a()&@#(!@!#$\t :) "
print(asc.isascii())

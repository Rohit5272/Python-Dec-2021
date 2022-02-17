"""
List 

List is a sequence in python. 
It can store any type of data separated by ',' enclosed in '[]'

Syntax:

[element1, element2, ....]

"""

l = [1, 2, 3, 4, 5]

print(type(l))

print(l)
print(id(l))

l1 = l

print(l1)
print(id(l1))

l1.append("End")

print()
print(l, id(l))
print(l1, id(l1))
print()
l2 = [1, 2, 3, 4, 5]

print(id(l2))
print(l2)


a = 20
b = a
print("a", a, id(a))
print("b", b, id(b))

print()
b = b + 1
print("a", a, id(a))
print("b", b, id(b))


l = ["a", 5.5, 9, 3+4j, True, [1, 2, 3]]  # list can store any type of data
print(l)

print(l[:])
print(l[2:5])
print(l[-3:-1])  # start end+1
print()

# accessinf elements from list
print(l[1])
print(l[5], l[-1], l[len(l)-1])
print()

# update elements from list
l[0] = "A"
print(l)

k = [1, 2, 3]
print(k, id(k))
k = [4, 5, 6]
print(k, id(k))

l[1:3] = 6.6, 10
print(l)

print()
# deleting values from list

a = 5
print(a)
del a  # del is keyword in python that can delete anything
# print(a)  -> NameError: name 'a' is not defined

print(k)
del k[0]  # [5,6]
print(k)

k = [1, 2, 3, 4, 5]
del k[1:3]
print(k)


print()
# operators on the list

l2 = [9, 8, 7]

print(l)
print(l2)

l3 = l2+l+['a', 'b', 'c', ]
print(l3)

l3 = l2 * 2  # l2+l2+l2, values are repeated
print(l3)

l3 = 6.6 in l
print(l3)

print(len(l))

# functions on list
print(dir(l))

print(l)
l.reverse()  # inplace replacement
print(l)

st = "string"
print(dir(st))
print(st)
print(st.upper())  # temp = st, temp.upper -> return temp
print(st)

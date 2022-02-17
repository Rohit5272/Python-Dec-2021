print("### Immutable ###")
"""
When two variable with same values are created, same ids are created.
When any of the two variable is changed new id is created.
"""

a = 20
b = a
print("a", a, id(a))
print("b", b, id(b))

print()
b = b + 1
print("a", a, id(a))
print("b", b, id(b))

print("### Mutable ###")
"""
When two variable with same values are created, different ids are created.
When any of the two variable is changed id remains name but values of both changes.
"""

l = [1, 2, 3, 4, 5]

l1 = l

print(l, id(l))
print(l1, id(l1))


l1.append("End")

print()
print(l, id(l))
print(l1, id(l1))

print()

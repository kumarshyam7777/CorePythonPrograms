# Simple way to creating a set .
# A set does not support repeat
set_1 = {1, 1, 2, 2, 3, 3, 4, 4, 5, 5}
print(type(set_1))
print(set_1)

# Creating an empty set syntax is given below:
b = set()
print(type(b))

# adding an element to the empty set.
b.add(4)
b.add(5)
b.add(6)
b.add((1, 2, 3, 4, 1))
print(b)
print(len(b))

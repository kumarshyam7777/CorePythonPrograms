x = 10
print(id(x))
x = x+1
print(id(x))

a = 100.541
b = 100.541
print(a is b)
print(id(a))
print(id(b))

comp1 = 5 + 4j
comp2 = 5 + 4j
print(id(comp1))
print(id(comp2))

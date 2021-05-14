list1 = [10, 20, 30, 40]
b = bytearray(list1)
print(type(b))
for i in b:
    print(i)
b[0] = 100     # bytearray is mutable object
b[1] = 120

for j in b:
    print(j)


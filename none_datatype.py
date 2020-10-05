a = None
b = None
c = None


def fun():
    pass


d = fun()


def printFun():
    print("Hello Awesome Python")
    return 30+12


m = printFun()
print(m)


print(id(a), id(b), id(c), id(d))

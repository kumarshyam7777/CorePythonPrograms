string = 'abcdefghijklmnopqrstuvwxyz'
# If the begin and end index is there it takes upto starting to end - 1
print(string[3:9])
# If the begin index is missing then the it starts from zero
print(string[:25])
# If the end index is missing then it goes upto end of the string
print(string[3:])
# If the begin index and end index both arte missing then it consider the whole string as it is
print(string[:])
# Slice operator never rise indexError : It takes upto last of the string
print(string[3:100])
# It takes as empty string
print(string[3:1])
print("Hello")

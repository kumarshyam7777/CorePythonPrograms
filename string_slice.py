string = 'abcdefghijklmnopqrstuvwxyz'
print(string[0:30])
# If the begin and end index is there it takes up to starting to end - 1
print(string[3:9])
# The below example shows the starting from 0 means a to (7-1) = 6 means up to 6
print(string[0:7])
# If the begin index is missing then the it starts from zero up to last index of the string.
print(string[:25])
# If the end index is missing then it goes up to end of the string
print(string[3:])
# If the begin index and end index both are missing then it consider the whole string as it is
print(string[:])
# Slice operator never rise indexError : It takes up to last of the string
print(string[3:100])
# It takes as empty string
print(string[3:1])
print("Hello")

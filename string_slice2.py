s = 'durga'
output = s[0].upper()+s[1:]
print(output)

str = 'shyam'
output = str[:len(str)-1] + str[-1].upper()
print(output)

string = 'jayanta'
output = string[0].upper()+string[1:len(string)-1]+string[-1].upper()
print(output)

name_char = 'ShyamIsGood'
changed_name = name_char[0::2]  # is same as name_char[0:12:2]
print(changed_name)
changed_name_1 = name_char[::2]  # is same as name_char[0:12:2]
print(changed_name_1)
# is same as name_char[0:12(Means len(name_char)+1):2]
changed_name_2 = name_char[:len(name_char)+1:2]
print(changed_name_2)
print(name_char[0::2], name_char[::2], name_char[:len(name_char)+1:2])
print(name_char[:-1:2])

dict = {
    1: 2,
    'name': 'shyam',
    'profession': 'Python Programmer',
    list: [20, 40, 60, 80]
}

print(type(dict))
print(dict.keys())  # Prints the key of the Dictionary
print(type(dict.keys()))
print(list(dict.keys()))  # Covertys the dict_keys to list
print(tuple(dict.keys()))  # Converts the dict_keys to tuple
print(dict.values())
print(type(dict.values()))
print(list(dict.values()))  # Converts the dict_values to list type
print(tuple(dict.values()))  # Converts the dict_values to tuple type
print(dict.items())  # Prints the (key,value) for all contents of the dictionary
# this is a way to upadte the methods into another variable and apply update method to the existing dict
updateDict = {
    'friends': ['Sugandha', 'Abichal', 'Mudita']
}
dict.update(updateDict)
print(dict)  # Update the dictionary by adding key-value pairs from updateDict
updateDict_1 = {
    'Electrnics Accessories': ("Motorola Mobile", "HP Laptop", "WD External HDD"),
    'Python': 'Dynamically Typed Programming language',
    'Java': 'Java is a object Oriented Programming language'
}
dict.update(updateDict_1)
print(dict)  # Update the dictionary by adding key-value pairs from updateDict

# .get() method prints the value which are associated with 'Electrnics Accessories'
print(dict.get('Electrnics Accessories'))

print(dict['Electrnics Accessories'])

# Difference between the .get() method and the [] method
print(dict.get('Electronics Accessories'))
# throws an error as Electronis Accessories is not present in dictionary
# print(dict['Electronics Accessories'])

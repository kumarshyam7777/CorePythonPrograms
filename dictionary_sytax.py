myDict = {
    "name": "shyam",
    "profession": "React Developer",
    list: [10, 20, 30],
    tuple: (10, 20, 30),
    "secondDict": {
        "degree": "MCA",
        "CGPA": 6.86,
        "college": "ITM UNIVERSITY GWALIOR",
        "thirdDict": {
            "bachelor": 'BCA',
            "CGPA": 6.56,
            'college': 'ASANSOL ENGINEERING COLLEGE'
        }
    }
}
# print(type(myDict))
# print(myDict)
# print(myDict.get("name"))
# myDict.update()
# print(myDict[list])
# print(myDict[tuple])
# print(myDict['profession'])
# print(myDict['secondDict']['college'])
# print(myDict['secondDict']['thirdDict'])
print(myDict.values())
# print(myDict.items())

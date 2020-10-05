myHindiDict = {
    'saman_rakhne_ki_cheezein': 'containers',
    'jana': 'go',
    'aana': 'come'
}
print("Yours options are", myHindiDict.keys())
a = input("Enter the Hindi Words\n")
print("Your English Meaning word is: ", myHindiDict[a])
print("Your English Meaning word is: ", myHindiDict.get(a))

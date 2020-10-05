letter = ''' Dear <|NAME|>, 
 You are selected as Software Developer at our Companny, TechnoWorld.
 We are happy to inform you about your selection with this offer letter.

 Thanks & Regards
 Durga,
 Date : <|DATE|>
'''
name = input("Enter your name!")
date = input("Enter the date!")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)

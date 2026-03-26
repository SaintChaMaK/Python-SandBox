####  Challenge: Turn Your User Into a L33t H4x0r

"""
Write a script called translate.py that asks the user for some input
with the following prompt: Enter some text:. Then use the .replace()
method to convert the text entered by the user into “leetspeak” by making the 
following changes to lower-case letters:
• The letter a becomes 4
• The letter b becomes 8
• The letter e becomes 3
• The letter l becomes 1
• The letter o becomes 0
• The letter s becomes 5
• The letter t becomes 7
Your program should then display the resulting string as output. 
Below is a sample run of the program:

Enter some text: I like to eat eggs and spam.
I 1ik3 70 347 3gg5 4nd 5p4m.

"""
translate = input("Enter some text: ")
#repTranslate = translate.replace("a", "4")
#repTranslate = repTranslate.replace("b", "8")
#repTranslate = repTranslate.replace("e", "3")
#repTranslate = repTranslate.replace("l", "1")
#repTranslate = repTranslate.replace("o", "0")
#repTranslate = repTranslate.replace("s", "5")
#repTranslate = repTranslate.replace("t", "7")
#print(repTranslate)

repTranslate = translate.replace("a", "0")
repTranslate = repTranslate.replace("e", "3")
repTranslate = repTranslate.replace("l", "L")
repTranslate = repTranslate.replace("o", "0")
repTranslate = repTranslate.replace("s", "H")
repTranslate = repTranslate.replace("p", "4")
repTranslate = repTranslate.replace("k", "r")

print(repTranslate)


#### End of the challenge               ####
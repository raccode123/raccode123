
#ask the user to enter a sentence using the input method.
#save the users input to a variable called str_manip
#Use this string value write the code to do the following 
#1 calculate and display the string length
#2 find the last letter of in str_manip sentence, replace every occurence with the '@'
#3 print the last 3 characters in str_manip backwaddsd
#4 create a five ltter word that is made up of the first three characters and the last two characters in str_manip


#user input

str_manip=input("Enter sentence here: ")

#1 calculate and display the string length

str_manip_len=len(str_manip)
print(str_manip_len)

#2 find the last letter of in str_manip sentence, replace every occurence with the '@'
char_replace=str_manip[-1]
print(str_manip.replace(char_replace, "@"))

#3 print the last 3 characters in str_manip backwaddsd

print(str_manip[:-4:-1])

#4 create a five ltter word that is made up of the first three characters and the last two characters in str_manip

print(str_manip[:3]+str_manip[-2:])
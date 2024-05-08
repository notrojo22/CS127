#Rojas Shrestha
#rojas.shrestha85@myhunter.cuny.edu
#March 19, 2024
#This program prompts the user to input a list of words then outputs the total number of words and the ratio of plural words to total words

word = input("Enter a list of words: ")
wordspace = word.count(' ') + 1
wordS = word.count('s ')

if word[-1] == ("s"):
     wordS = wordS + 1

wordfraction = wordS / wordspace

print ("The total amount of words is:", wordspace)
print ("The fraction of your list that is plural is: ", wordfraction)















#Rojas Shrestha
#rojas.shrestha85@myhunter.cuny.edu
#March 5, 2024
#This program asks the user to input a string and outputs a pyramid using the letters in the input.

s = str(input("Enter a string to be turned into a pyramid: "))
ls = len(s)

for i in range (0,ls):
    for j in range (i+1):
        print(s[j], end = "")
    print()
for i2 in range (ls,0,-1):
    for j2 in range (i2-1):
        print (s[j2], end = "")
    print()

#Rojas Shrestha
#rojas.shrestha85@myhunter.cuny.edu
# April 1, 2024
# This program groups names from an input

name_list = input("Enter a list of names: ")

nls = name_list.split("; ")
print (nls)

for name in nls:
    nls2 = name.split(", ")
    print (nls2)

nls3 = nls2[0].split(" ")
print (nls3) 

print (nls2[1], nls3[1], nls3[0])


print ("Thank you for using my name organizer!")



   


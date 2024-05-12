#Rojas Shrestha
#rojas.shrestha85@myhunter.cuny.edu
#March 4, 2024
#This program prompts the user to input a message then prints out the message in reverse with 2 columns per output line

Message = input("Enter a phrase to be reversed ")
length = (len(Message)-1)

for i in range (length,-1,-1):
    print (Message[i],Message[i])
 
print("Thank you for playing! ")

#Rojas Shrestha
#rojas.shrestha85@myhunter.cuny.edu
#April 2, 2024
#This program prints out a greeting based on the respective time of day 

current_time = int(input("Enter a time of day (in 24 hour time): "))
if current_time < 12:
    print ("Good morning")
elif current_time in range (11,17):
    print ("Good afternoon")
else:
    print ("Good evening")




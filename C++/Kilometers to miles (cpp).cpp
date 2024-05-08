// Rojas Shrestha
// rojas.shrestha85@myhunter.cuny.edu
// Arpil 25, 2024
// This program converts kilometers to miles

#include <iostream>
using namespace std; 

int main()
{
double kilometers, miles; 
cout << "Enter an amount of kilometers: ";    
cin >> kilometers;       
miles = kilometers * 0.621371;
cout << "The kilometers you entered converted into miles is: " << miles; 
return 0;
}
//Rojas Shrestha
//rojas.shrestha85@myhunter.cuny.edu
//April 26, 2024
//This program checks if the year entered by the user is 2018 or less

#include <iostream>
using namespace std; 

int main()
{
    int input;
    cout << "Enter a year: ";
    cin >> input;
    while (input > 2018)
    {
     cout << "Year must be 2018 or earlier: ";
     cin >> input;
    }
    else if (input <= 2018) {
    cout << "You entered: " << input;
    }
 
    return 0; 
}
//Rojas Shrestha
//rojas.shrestha85@myhunter.cuny.edu
//April 26, 2024
// This program outputs seasonal greetings based on the number of month entered

#include <iostream>
using namespace std;

int main(){
    int month;
    cout << "Enter month (as a number): ";
    cin >> month;
    if (month < 3 or month > 11) {
        cout << "Happy Winter";
    }
    if (month <= 3 or month < 7) {
        cout << "Happy Spring";
    }
    if (month >= 7 && month < 9){
        cout << "Happy Summer";
    }
    else{
        cout << "Happy Fall";
    }
    return 0;
}
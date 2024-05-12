//Rojas Shrestha
//rojas.shrestha95@myhunter.cuny.edu
//May 1, 2024
//This program prints a number in two complements form

#include <iostream>
using namespace std;

int main () {
    int b = 16;    
    int x;
    int n; 
        cout << "Enter a number: "; 
        cin >> n;
    if (n < 0) {
        cout << "1";
        x = 32 + n;
    }
    else if (n >= 0) { 
        cout << "0";
        x = n;
    } 
    while (b > 0.5) {
        if (x >= b){
            cout << "1";
        }
        else {
            cout << "0";
        }
        x = x % b;
        b = b/2; 
    }
    cout << "/n";
    return 0;
 }
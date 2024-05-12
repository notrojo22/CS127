//Rojas Shrestha
//rojas.shrestha85@myhunter.cuny.edu
//May 1, 2024
//This program tracks the USA population from the year 2017

#include <iostream>
using namespace std;

int main(){
    int year = 2017; 
    float population = 325.7;
    int time;
        cout << "Please enter the number of years: ";
        cin >> time;
    double death = 0.0084, birth = 0.0124;
    int i; 
        for (i = 0; i < time; i++){
            cout << "Year " << year << " " << population;
            population = population + (birth * population) - (death * population);
            year = ++year;
            cout << "\n";
        }
    return 0; 
}

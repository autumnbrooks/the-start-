#include <iostream>
#include<string>
using namespace std;
int main() {
  string city1 , city2, city3 ;
  double cityOneTemp, cityOneTemp2, cityOneTemp3;
  double cityTwoTemp,cityTwoTemp2, cityTwoTemp3;
  double cityThreeTemp, cityThreeTemp2, cityThreeTemp3;
  ///averages of reg and increased temperatures
  double city1Av, city2Av, city3Av;
  double average, average2, average3;
  cout<<"Enter Your First City Below ☟"<<endl; 
  cin >> city1;
  cout<< "Enter "<<city1<<"\'s Temperature ☂︎ : "<<endl; 
  cin >> cityOneTemp;
  cout << "Enter "<<city1<<"\'s Temperature ☂︎ : "<<endl; 
  cin >> cityOneTemp2;
  cout << "Enter "<<city1<<"\'s Temperature ☂︎ : "<<endl; 
  cin >> cityOneTemp3;
  cout << "Enter Your Second City Below ☟ ", cout<<endl; 
  cin >> city2;
  cout << "Enter "<<city2<<"\'s Temperature : "<<endl; 
  cin >> cityTwoTemp;
  cout << "Enter "<<city2<<"\'s Temperature : "<<endl;
  cin >> cityTwoTemp2;
  cout << "Enter "<<city2<<"\'s Temperature : "<<endl;
  cin >> cityThreeTemp;
  cout << endl;
  cout << "Enter You Third City Below ☟ " << endl; 
  cin >> city3;
  cout << "Enter " << city3<<"\'s Temperature : " << endl; 
  cin >> cityThreeTemp;
  cout << "Enter "<< city3<<"\'s Temperature : " << endl;
  cin >> cityThreeTemp2;
  cout << "Enter " << city3 << "\'s Temperature : "<< endl;
  cin >> cityThreeTemp3;
  city1Av = (cityOneTemp + cityOneTemp2 + cityOneTemp3)/3;
  city2Av=(cityTwoTemp + cityTwoTemp2 + cityThreeTemp2)/3;
  city3Av=(cityThreeTemp + cityThreeTemp2 + cityThreeTemp2)/3;
  average = city1Av * 1.03;
  average2 = city2Av * 1.03;
  average3 = city3Av * 1.03;
  cout<< "The average temp in "<< city1 << " is " << city1Av << endl ;
  cout<< endl;
  cout<<"The increased average temp in "<<city1<<" is "<< city2Av << endl;
  cout<<endl;
  cout<<"The average temp in "<< city2 <<" is " << city2Av << endl;
  cout<<endl;
  cout<<"The average temp in "<< city3 <<" is "<< city3Av <<endl;
  cout<<"The increased average in "<< city2 <<" is "<< average2 <<endl;
  cout<<endl;
  cout<<"The increased avergae temp in "<< city3 << " is "<< average3 <<endl;
  cout<<endl;
  return 0; }


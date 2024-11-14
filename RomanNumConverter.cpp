#include <iostream>
#include <string>
#include <map>
using namespace std;

// Function to convert Roman numeral to integer using a map
int romanToInt(const string& roman) {
    // Create a map of Roman numerals to integer values
    map<char, int> romanMap = {
        {'I', 1}, {'V', 5}, {'X', 10}, {'L', 50},
        {'C', 100}, {'D', 500}, {'M', 1000}
    };
    
    int result = 0;
    
    // Loop through the Roman numeral string
    for (int i = 0; i < roman.length(); i++) {
        // Check if we are in a subtraction case
        if (i + 1 < roman.length() && romanMap[roman[i]] < romanMap[roman[i + 1]]) {
            result -= romanMap[roman[i]]; // Subtract current value if next is larger
        } else {
            result += romanMap[roman[i]]; // Add the value if next is equal or smaller
        }
    }
    
    return result;
}

// Function to convert integer to Roman numeral using a map
string intToRoman(int num) {
    // Create a map of integer values to Roman numerals
    map<int, string> romanMap = {
        {1000, "M"}, {900, "CM"}, {500, "D"}, {400, "CD"},
        {100, "C"}, {90, "XC"}, {50, "L"}, {40, "XL"},
        {10, "X"}, {9, "IX"}, {5, "V"}, {4, "IV"}, {1, "I"}
    };
    
    string result = "";
    
    // Loop through the map and subtract values from num
    for (auto& pair : romanMap) {
        while (num >= pair.first) {
            result += pair.second;
            num -= pair.first;
        }
    }
    
    return result;
}

// Function to display the user menu
void showMenu() {
    cout << "\nSelect an option:" << endl;
    cout << "1. Convert Roman Numeral to Numeric" << endl;
    cout << "2. Convert Numeric to Roman Numeral" << endl;
    cout << "3. Exit" << endl;
}

int main() {
    int choice;
    string input;
    
    while (true) {
        showMenu();
        cout << "Enter your choice: ";
        cin >> choice;
        
        if (choice == 1) {
            cout << "Enter a Roman Numeral: ";
            cin >> input;
            int numericValue = romanToInt(input);
            cout << "Roman Numeral " << input << " is equal to " << numericValue << endl;
        }
        else if (choice == 2) {
            int numericValue;
            cout << "Enter a numeric value: ";
            cin >> numericValue;
            if (numericValue <= 0 || numericValue > 3999) {
                cout << "Please enter a number between 1 and 3999." << endl;
            } else {
                string romanNumeral = intToRoman(numericValue);
                cout << "Numeric value " << numericValue << " is equal to Roman Numeral " << romanNumeral << endl;
            }
        }
        else if (choice == 3) {
            cout << "Exiting program." << endl;
            break;
        }
        else {
            cout << "Invalid choice. Please try again." << endl;
        }
    }

    return 0;
}

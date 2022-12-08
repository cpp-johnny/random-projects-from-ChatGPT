#include <iostream>
#include <string>
#include <bitset>

using namespace std;

int main() {
    string phrase;

    cout << "Enter a phrase: ";
    getline(cin, phrase);

    // Loop through each character in the phrase
    for (char c : phrase) {
        // Convert the character to a string of bits and print it
        cout << bitset<8>(c).to_string() << " ";
    }

    cout << endl;

    return 0;
}

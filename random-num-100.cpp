#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
    srand(time(0));
    int randomNumber = rand() % 100 + 1;

    cout << "The random number is: " << randomNumber << endl;

    return 0;
}

#include <iostream>
#include <chrono>
#include <thread>

using namespace std;

int main() {
    cout << "Press Enter to start the stopwatch" << endl;
    cin.get();

    // Get the current time
    auto start = chrono::high_resolution_clock::now();

    cout << "Press Enter to stop the stopwatch" << endl;
    cin.get();

    // Get the current time
    auto end = chrono::high_resolution_clock::now();

    // Calculate the elapsed time
    auto elapsed = end - start;

    cout << "Elapsed time: " << chrono::duration_cast<chrono::seconds>(elapsed).count() << " seconds" << endl;

    return 0;
}

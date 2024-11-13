#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> fib = {1, 1};
    int sum = 0;

    while (fib.back() < 4'000'000) {
        int n = fib.size();
        fib.push_back(fib[n - 1] + fib[n - 2]);
       
        if (fib.back() % 2 == 0) 
            sum += fib.back();
    }

    cout << "Sum of even Fibonacci numbers: " << sum << endl;
    return 0;
}

#include <iostream>
#include <vector>
#include <cmath> 

using namespace std;

int get_fuel(vector <int> crabs, int align) {
    int total = 0;
    for (int i = 0; i < crabs.size(); i++) {
        int n = abs(align - crabs[i]);
        total += (n * (n + 1)) / 2;
    }
    return total;
}

int main() {
    vector <int> crabs;
    int crab;

    while (cin >> crab) {
        crabs.push_back(crab);
        cin.ignore(1);
    }

    sort(crabs.begin(), crabs.end());
    int mini = 0;
    int maxi = crabs.size();
    int cur_min = get_fuel(crabs, crabs[mini]);
    int cur_max = get_fuel(crabs, crabs[maxi]);
    long long efficient = 0;
    
    while (mini != maxi) {
        if (cur_min < cur_max) {
            efficient = cur_min;
            maxi -= 1;
            cur_max = get_fuel(crabs, maxi);
        }
        else {
            efficient = cur_max;
            mini += 1;
            cur_min = get_fuel(crabs, mini);
        }
    }
    cout << efficient << endl;
}



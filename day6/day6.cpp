#include <iostream>

using namespace std;
#define D 256

long long get_total(int first) {
    long long total = 1;
    long long modCount[D][7] = {0};
    modCount[0][first] = 1;
    for (int i = 1; i < D; i++) {
        int parent = i % 7;
        int child = (i + 2) % 7;
        for (int j = 0; j < 7; j++) {
            modCount[i][j] += modCount[i - 1][j];
        }
        total += modCount[i][parent];
        if (i + 3 < D) {
            modCount[i + 3][child] += modCount[i][parent];
        }
    }
    return total;
}

int main() {
    long long modTotal[5] = {0};
    for (int i = 0; i < 5 ; i++) {
        modTotal[i] = get_total(i + 1);
    }
    long long total = 0;

    int fish;
    while (cin >> fish) {
        total += modTotal[fish - 1];
        cin.ignore(1);
    }

    cout << total << endl;
}

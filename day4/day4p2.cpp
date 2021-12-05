#include <bits/stdc++.h>

using namespace std;

int main() {
    string s;
    cin >> s;
    vector<int> nums;

    string full_num = "";
    int n = 0;

    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] == ',')
        {
            nums.push_back(stoi(full_num));
            full_num = "";
            n += 1;
        }
        else
        {
            full_num += s[i];
        }
    }
    nums.push_back(stoi(full_num));
    vector<vector<vector<int>>> N(100, vector<vector<int>> (5, vector<int> (5)));
    vector<vector<vector<int>>> taken(100, vector<vector<int>>(5, vector<int>(5)));
    vector<vector<int>> rowMax(100, vector<int>(5));
    vector<vector<int>> colMax(100, vector<int>(5));

    for (int b = 0; b < 100; b++) {
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                int x;
                cin >> x;
                N[b][i][j] = x;
                
                auto it = find(nums.begin(), nums.end(), x);
                if (it == nums.end()) {
                    taken[b][i][j] = 0;
                    cout << x << "PROBLEM! \n";
                }
                else {
                    int num = it - nums.begin() + 1;
                    taken[b][i][j] = num;
                }
                if (j == 4) {
                    // look at row
                    rowMax[b][i] = taken[b][i][4];
                    for (int k = 0; k < 5; k++) {
                        if (taken[b][i][k] > rowMax[b][i]) {
                            rowMax[b][i] = taken[b][i][k];
                        }
                    }
                }
                if (i == 4) {
                    colMax[b][j] = taken[b][4][j];
                    for (int k = 0; k < 5; k++) {
                        if (taken[b][k][j] > colMax[b][j]) {
                            colMax[b][j] = taken[b][k][j];
                        }
                    }
                }
            }
        }
    }

    int bingo_max_val = 0;
    int bingo_max_board = 0;

    for (int b = 0; b < 100; b++)
    {
        int board_bingo = rowMax[b][0];

        for (int line = 0; line < 5; line++)
        {
            if (rowMax[b][line] < board_bingo) {
                board_bingo = rowMax[b][line];
            }
            if (colMax[b][line] < board_bingo) {
                board_bingo = colMax[b][line];
            }
        }
        if (bingo_max_val < board_bingo) {
            bingo_max_val = board_bingo;
            bingo_max_board = b;
        }
    }

    int max_called = bingo_max_val;
    int max_called_val;
    int sum_uncalled = 0;

    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            if (taken[bingo_max_board][i][j] > max_called)
            {
                sum_uncalled += N[bingo_max_board][i][j]; 
            }
            if (taken[bingo_max_board][i][j] == max_called) {
                max_called_val = N[bingo_max_board][i][j]; 
            }
        }
    }

    int ans = max_called_val * sum_uncalled;
    cout << "ANS: " << ans << endl;
}

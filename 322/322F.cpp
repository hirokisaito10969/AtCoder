#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<int> process_queries(int N, int Q, string S, vector<vector<int>>& queries) {
    vector<int> results;
    int ones_count = 0;
    for (char c : S) {
        if (c == '1') ones_count++;
    }

    for (auto& query : queries) {
        int c = query[0], L = query[1], R = query[2];
        if (c == 1) {
            for (int i = L - 1; i < R; i++) {
                if (S[i] == '1') {
                    ones_count--;
                    S[i] = '0';
                } else {
                    ones_count++;
                    S[i] = '1';
                }
            }
        } else {
            string T = S.substr(L - 1, R - L + 1);
            size_t max_ones = 0;
            size_t current_ones = 0;
            for (char c : T) {
                if (c == '1') {
                    current_ones++;
                } else {
                    max_ones = max(max_ones, current_ones);
                    current_ones = 0;
                }
            }
            max_ones = max(max_ones, current_ones);
            results.push_back(max_ones);
        }
    }

    return results;
}

int main() {
    int N, Q;
    cin >> N >> Q;
    string S;
    cin >> S;
    vector<vector<int>> queries(Q, vector<int>(3));
    for (int i = 0; i < Q; i++) {
        for (int j = 0; j < 3; j++) {
            cin >> queries[i][j];
        }
    }

    vector<int> results = process_queries(N, Q, S, queries);
    for (int result : results) {
        cout << result << endl;
    }

    return 0;
}

// 9 AC 9 TLE compile error
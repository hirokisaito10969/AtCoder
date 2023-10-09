#include <iostream>
using namespace std;

bool is_321_like(int num) {
    string str_num = to_string(num);
    for (size_t i = 0; i < str_num.length() - 1; i++) {
        if (str_num[i] <= str_num[i + 1]) {
            return false;
        }
    }
    return true;
}

int find_kth_321_like_number(int K) {
    int current_num = 1;
    while (K > 0) {
        if (is_321_like(current_num)) {
            K--;
        }
        current_num++;
    }
    return current_num - 1;
}

int main() {
    int K;
    cin >> K;
    int result = find_kth_321_like_number(K);
    cout << result << endl;
    return 0;
}

// AC 28 TLE 5
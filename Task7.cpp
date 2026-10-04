#include <iostream>
#include <vector>
using namespace std;

bool good(int x, int k, vector<int> a) {
    int cnt = 0;

    for (int len : a) {
        cnt += len / x;
    }

    return cnt >= k;
}

int main() {
    int n, k;
    cin >> n >> k;

    vector<int> a(n);

    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    int l = 0;
    int r = 10000001;

    while (r - l > 1) {
        int m = (l + r) / 2;

        if (good(m, k, a)) {
            l = m;
        } else {
            r = m;
        }
    }

    cout << l << endl;

    return 0;
}
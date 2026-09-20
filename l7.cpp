#include <iostream>
#include <vector>
using namespace std;

void CountSort(vector<int>& A) {
    int count[101] = {};

    for (int i = 0; i < A.size(); i++) {
        count[A[i]]++;
    }

    int k = 0;

    for (int i = 0; i <= 100; i++) {
        while (count[i] > 0) {
            A[k] = i;
            k++;
            count[i]--;
        }
    }
}

int main() {
    vector<int> A;
    int x;

    while (cin >> x) {
        A.push_back(x);
    }

    CountSort(A);

    for (int i = 0; i < A.size(); i++) {
        cout << A[i] << " ";
    }

    return 0;
}
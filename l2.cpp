#include <iostream>
#include <vector>
using namespace std;

void InsertionSort(vector<int>& A) {
    int n = A.size();

    for (int i = 1; i < n; i++) {
        int key = A[i];
        int j = i;

        while (j >= 1 && A[j - 1] > key) {
            A[j] = A[j - 1];
            j--;
        }

        A[j] = key;
    }
}

int main() {
    vector<int> A;
    int x;

    while (cin >> x) {
        A.push_back(x);
    }

    InsertionSort(A);

    for (int i = 0; i < A.size(); i++) {
        cout << A[i] << " ";
    }

    return 0;
}
#include <iostream>
#include <vector>
#include <sstream>
using namespace std;

void SelectionSort(vector<int>& A) {
    int n = A.size();

    for (int i = 0; i < n - 1; i++) {
        int max = A[i];
        int ind = i;

        for (int j = i + 1; j < n; j++) {
            if (A[j] > max) {
                max = A[j];
                ind = j;
            }
        }

        if (i != ind) {
            int temp = A[i];
            A[i] = A[ind];
            A[ind] = temp;
        }
    }
}

int main() {
    vector<int> A;
    string line;

    getline(cin, line);

    stringstream ss(line);
    int x;

    while (ss >> x) {
        A.push_back(x);
    }

    SelectionSort(A);

    for (int i = 0; i < A.size(); i++) {
        cout << A[i] << " ";
    }

    return 0;
}
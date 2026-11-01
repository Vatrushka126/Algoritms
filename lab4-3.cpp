#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Heap {
private:
    vector<int> heap;

    void sift_down(int i) {
        int n = heap.size();

        while (true) {
            int left = 2 * i + 1;
            int right = 2 * i + 2;
            int smallest = i;

            if (left < n && heap[left] < heap[smallest])
                smallest = left;

            if (right < n && heap[right] < heap[smallest])
                smallest = right;

            if (smallest == i)
                break;

            swap(heap[i], heap[smallest]);
            i = smallest;
        }
    }

public:
    void clear() {
        heap.clear();
    }

    void add(int n) {
        heap.push_back(n);
        int i = heap.size() - 1;

        while (i > 0) {
            int parent = (i - 1) / 2;

            if (heap[parent] <= heap[i])
                break;

            swap(heap[parent], heap[i]);
            i = parent;
        }
    }

    void extract() {
        if (heap.empty()) {
            cout << "CANNOT\n";
            return;
        }

        cout << heap[0] << '\n';

        heap[0] = heap.back();
        heap.pop_back();

        if (!heap.empty())
            sift_down(0);
    }
};

int main() {
    Heap h;
    string command;

    while (cin >> command) {
        if (command == "CLEAR") {
            h.clear();
        } 
        else if (command == "ADD") {
            int n;
            cin >> n;
            h.add(n);
        } 
        else if (command == "EXTRACT") {
            h.extract();
        }
    }

    return 0;
}
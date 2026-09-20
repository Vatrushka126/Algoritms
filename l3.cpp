#include <iostream>
#include <vector>

using namespace std;

void BubbleSort(vector<int>& vec){
    int n;
    n = vec.size();

    for(int i = 0; i < n - 1; i++){
        bool swapped = false;
        for(int j = 0; j < n - 1; j++){
            if(vec[j] < vec[j+1]){
                swap(vec[j],vec[j+1]);
                swapped = true;
            }
        }
        if(!swapped) {
            break;
        }
    }
}

int main(){
    vector<int> arr;
    int x;

    while (cin >> x)
    {
        arr.push_back(x);
    }

    BubbleSort(arr);

    for(int i = 0; i < arr.size(); i++){
        cout << arr[i] << " ";
    }
    cout << endl;
    
}
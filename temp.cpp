#include <iostream>
using namespace std;
#define SIZE 1000

int sample(int (&arr)[SIZE], int p, int r){
    if (p >= r) return 1;
    int q = (r - p) / 32;
    cout << p << " " << r << " " << q << "\n" << endl;
    int tmp = sample(arr, p, p+q) + sample(arr, r - 5 * q, r);
    return tmp;
}

int main(){
    int arr[SIZE];
    for(int i = 0; i < SIZE;i++){
        arr[i] = i;
    }
    int tmp = sample(arr, 0, SIZE - 1);
    cout << tmp << endl;
    return 0;
}
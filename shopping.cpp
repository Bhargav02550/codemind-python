#include <bits/stdc++.h>
using namespace std;
int fun(vector<int>& cart) {
    int n = cart.size();
    if (n == 0) {
        return -1;
    }
    int totalSum = accumulate(cart.begin(),cart.end(),0);
    int leftSum = 0;
    for (int i = 0; i < n; i++) {
        totalSum -= cart[i];
        if (leftSum == totalSum) {
            return i;
        }
        leftSum += cart[i];
    }
    return -1;
}
int main() {
    int T;
    cin >> T;
    while(T--) {
        int N;
        cin >> N;
        vector<int> cart(N);
        for (int i = 0; i < N; i++) {
            cin >> cart[i];
        }
        int res = fun(cart);
        cout << res << endl;
    }
}

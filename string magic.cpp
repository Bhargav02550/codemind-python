#include<bits/stdc++.h>
using namespace std;
int main() {
    string s;
    cin >> s;
    int num = 0; 
    int totalSum = 0;
    bool isNegative = false;
    for (char ch : s) {
        if (isdigit(ch)) num=num*10+(ch-'0');
        else if (ch == '-') isNegative = true;
        else{
            if(isNegative) {
                num *= -1;
            }
            totalSum += num;
            num = 0;
            isNegative = false;
        }
    }
    if (isNegative) {
        num *= -1;
    }
    totalSum += num;
    cout<<totalSum;
}

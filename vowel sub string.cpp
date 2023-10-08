#include<bits/stdc++.h>
using namespace std;
bool isVowel(char c) {
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}
int fun(string s) {
    int ans = 0;
    int n = s.size();
    for (int i = 0; i < n; i++) {
        unordered_set<char> st;
        for (int j = i; j < n; j++) {
            char ch = s[j];
            if (!isVowel(ch)) break;
            st.insert(ch);
            ans += st.size() == 5;
        }
    }
    return ans;
}
int main(){
    string s;
    cin>>s;
    int res=fun(s);
    cout<<res;
}

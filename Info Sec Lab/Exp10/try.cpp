#include <bits/stdc++.h>
using namespace std;

int a = 18;

int inc(int a){
    a = a + 123;
    return a;
}

int main(){
    a = inc(a);
    cout<<a;
}
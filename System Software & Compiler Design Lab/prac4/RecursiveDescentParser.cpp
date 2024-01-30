// null is symbolized by '^'

/*rules:
        S->cAd
        A->aA'
        A'->cA'| null
*/
#include <bits/stdc++.h>

using namespace std;

string st = "cacccc^d";
int stringPointer = 0;

//method: if you encounter a terminal, then increment the stringPointer then and there only
//        but if you encounter a variable, call its function, inside which you can increment the stringPointer ONLY after if conditions, not in the start!
//        if you call a function, and it returns back the control, then don't increment the stringPointer, as it is


//function prototypes
bool S(string st);
bool A(string st);
bool A_dash(string st);




bool S(string st){
    if (st[stringPointer] == 'c'){
        stringPointer ++;
        if (A(st) == true){
            if (st[stringPointer] == 'd'){
                stringPointer++;
                return true;
            }
            else return false;
        }
        else return false;
    }
    else return false;
}

bool A(string st){
    if (st[stringPointer] == 'a'){
        stringPointer++;
        if (A_dash(st) == true){
            return true;
        }
        else return false;
    }
    else return false;
}

bool A_dash(string st){
    if (st[stringPointer] == 'c'){
        stringPointer++;
        if (A_dash(st) == true){
            return true;
        }
        else{
            return false;
        }
    }
    else if (st[stringPointer] == '^'){
        stringPointer++;
        return true;
    }
    else return false;
}

int main(){

    if (S(st) == true) cout<<"Accepted";
    else cout<<"Not accepted";
    return 0;
}
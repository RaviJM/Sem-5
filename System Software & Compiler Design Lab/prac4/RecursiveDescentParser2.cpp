// null is symbolized by '^'

/*rules:
        E -> TE'
        E'-> +TE' | -TE' | null
        T -> FT'
        T'-> *FT' | null
        F -> i | (E)
*/
#include <bits/stdc++.h>

using namespace std;

string st = "i*i*(i*i^-i^^)*i*i^+i^^";
int stringPointer = 0;

//method: if you encounter a terminal, then increment the stringPointer then and there only
//        but if you encounter a variable, call its function, inside which you can increment the stringPointer ONLY after if conditions, not in the start!
//        if you call a function, and it returns back the control, then don't increment the stringPointer, as it is already incremented inside the called function


//function prototypes
bool E(string st);
bool E_dash(string st);
bool T(string st);
bool T_dash(string st);
bool F(string st);




bool E(string st){
    if (T(st) == true){
        if (E_dash(st) == true){
            return true;
        }
        else return false;
    }
    else return false;
}


bool E_dash(string st){
    if (st[stringPointer] == '+'){
        stringPointer++;
        if (T(st) == true){
            if (E_dash(st) == true){
                return true;
            }
            else return false;
        }
        else return false;
    }
    else if (st[stringPointer] == '-'){
        stringPointer++;
        if (T(st) == true){
            if (E_dash(st) == true){
                return true;
            }
            else return false;
        }
        else return false;
    }
    else if (st[stringPointer] == '^'){
        stringPointer++;
        return true;
    }
    else return false;
}


bool T(string st){
    if (F(st) == true){
        if (T_dash(st) == true){
            return true;
        }
        else return false;
    }
    else return false;
}


bool T_dash(string st){
    if (st[stringPointer] == '*'){
        stringPointer++;
        if (F(st) == true){
            if (T_dash(st) == true){
                return true;
            }
            else return false;
        }
        else return false;
    }
    else if (st[stringPointer] == '^'){
        stringPointer++;
        return true;
    }
    else return false;
}


bool F(string st){
    if (st[stringPointer] == 'i'){
        stringPointer++;
        return true;
    }
    else if (st[stringPointer] == '('){
        stringPointer++;
        if (E(st) == true){
            if (st[stringPointer] == ')'){
                stringPointer++;
                return true;
            }
            else return false;
        }
        else return false;
    }
    else return false;
}





int main(){

    if (E(st) == true) cout<<"Accepted";
    else cout<<"Not accepted";
    return 0;
}
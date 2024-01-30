#include <bits/stdc++.h>

using namespace std;

int T1 = 0;
int T2 = 1;


int gcd(int a, int b) {

    int temp;
    while (1){
        temp = a % b;
        if (temp == 0){
            return b;
        }
        a = b;
        b = temp;
    }
}

int extendedEuclidean(int a, int b){
    // a > b
    int A = a;
    int B = b;
    int Q = A/B;
    int R = A%B;

    int T = T1 - (T2*Q);

    // cout<<Q<<" "<<A<<" "<<B<<" "<<R<<" "<<T1<<" "<<T2<<" "<<T<<" "<<endl;

    A = B;
    B = R;
    T1 = T2;
    T2 = T;

    if (B == 0){
        return T1;
    }
    else{
        return extendedEuclidean(A, B);
    }
}

double powerMod(int plaintext, double power, double n){
    if (int(power) == 0) {
        return 1;
    }
    
    double result = powerMod(plaintext, power / 2, n);
    result = int(result * result) % int(n);
    
    if (int(power) % 2 == 1) {
        result = int(result * plaintext) % int(n);
    }
    
    return result;
}

int main() {

    double p = 3;
    double q = 7;

    double n = p * q;
    double phi = (p - 1) * (q - 1);

    double e = 2;
    
    // calculating value of e
    while (e < phi){
        // e must be co-prime to phi and
        // smaller than phi.
        if (gcd(e, phi) == 1)
            break;
        else
            e++;
    }

    // calculating value of d
    double d = extendedEuclidean(phi, e);
    while (d<0){
        d += phi;
    }
    

    cout<<"e: "<<e<<endl;
    cout<<"d: "<<d<<endl;
    cout<<"n: "<<n<<endl;

    int plaintext = 12;
    cout<<"Plaintext message: "<<plaintext<<endl;
    
    double cipherText = powerMod(plaintext,e,n);
    cout<<"Encrypted Text: "<<cipherText<<endl;

    double decryptedText = powerMod(cipherText,d,n);
    cout<<"Decrypted Text: "<<decryptedText<<endl;

    return 0;
}

// senders's authentication only

#include <bits/stdc++.h>
#include <cmath>

// used for generating digital signature
double PrivateP = 3;
double PrivateQ = 7;
double PrivateN = PrivateP * PrivateQ;
double phi = (PrivateP - 1) * (PrivateQ - 1);
double PrivateE = 2;

int T1 = 0;
int T2 = 1;

// used for encryption of message
double P = 5;
double Q = 7;
double N = P * Q;
double phi2 = (P - 1) * (Q - 1);
double E = 2;


using namespace std;

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

// to calculate inverse of a number
// to calculate value of d (inverse of e) modulo n
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

int calculateE(int PrivateE){
    // calculating value of PrivateE
    while (PrivateE < phi){
        // e must be co-prime to phi and
        // smaller than phi.
        if (gcd(PrivateE, phi) == 1){
            break;
        }
        else{
            PrivateE++;
        }
    }
    return PrivateE;
}

// to generate MD1 and MD2 for message m
int hashingFunction(string m){
    int hash = 0;
    for (char c : m){
        hash = (hash * 31) + c;
    }
    return hash;
}

// to generate digital signature for a md value generated in hashingFunction()
int generateDigitalSignature(int md){
    int k = 2;
    double PrivateD = extendedEuclidean(phi, PrivateE);
    T1 = 0;
    T2 = 1;
    while (PrivateD < 0){
        PrivateD += phi;
    }

    // cout<<phi<<endl;
    // cout<<PrivateE<<endl;
    // cout<<PrivateD<<endl;
    // cout<<PrivateN<<endl;

    // cout<<power<<endl;
    double power = pow((int)md, (int)(PrivateD));
    int power2 = int(power);
    double digitalSignature = power2 % int(PrivateN);
    return digitalSignature;
}

int decryptDigitalSignature(int digitalSignature){
    double PublicE = PrivateE;
    double PublicN = PrivateN;

    double power = pow((int)digitalSignature, (int)(PublicE));
    int power2 = int(power);

    int md = power2 % (int)PublicN;
    return md;
}

int checkAuthenticity(int originalMessage, int digitalSignature){
    int md = decryptDigitalSignature(digitalSignature);
    if (originalMessage == md){
        return true;
    }
    else{
        return false;
    }
}

int encryption(int originalMessage){
    double D = extendedEuclidean(phi2, E);
    while (D < 0){
        D += phi2;
    }
    double power = pow((int)originalMessage, (int)(E));
    int power2 = int(power);
    double cipherText = power2 % int(N);
    return digitalSignature;
}

int main() {
    // to calculate value of e which is needed by both Alice and Bob (sender & receiver)
    PrivateE = calculateE(PrivateE);
    E = calculateE(E);

    int originalMessage = 9;
    cout<<"Original message: "<<originalMessage<<endl;

    int digitalSignature = generateDigitalSignature(originalMessage);
    cout<<"Digital Signature generated: "<<digitalSignature<<endl;


    if (checkAuthenticity(originalMessage, digitalSignature)){
        cout<<"Authenication Successful!"<<endl;
    }
    else{
        cout<<"Authentication Failed!"<<endl;
    }

    return 0;
}

#include <bits/stdc++.h>
using namespace std;

void performEncryption(){
    cout << "Enter the encryption key: ";
    string key;
    cin >> key;
    int n = sqrt(key.length());
    vector<vector<int>> matrix(n, vector<int>(n));

	// filling the key matrix
    int iter = 0;
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            int val = key[iter] - 97;
            matrix[i][j] = val;
            iter++;
        }
    }

	// printing key matrix
    cout << "Key matrix:" << endl;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }

    cout << "Enter the message to encrypt: ";
    string message;
    cin >> message;

	// adding padding in message to fill in extra spaces
    int padding = (n - message.size() % n) % n;
    for (int i = 0; i < padding; i++){
        message += 'x';
    }

	// forming encrypted text
    int k = 0;
    string encryptedText = "";
    while (k < message.size()){
        for (int i = 0; i < n; i++){
            int sum = 0;
            int temp = k;
            for (int j = 0; j < n; j++){
                sum += (matrix[i][j] % 26 * (message[temp++] - 'a') % 26) % 26;
                sum = sum % 26;
            }
            encryptedText += (sum + 'a');
        }
        k += n;
    }
    cout << "\nEncrypted text is: " << encryptedText << '\n';
}

// function to calculate a mod(m)
int modInverse(int a, int m){
    a = a % m;
    for (int x = -m; x < m; x++)
        if ((a * x) % m == 1)
            return x;
	return 0;
}

// function that calculates a cofactor matrix 'temp' of matrix 'a' excluding the row 'p' and column 'q'
void getCofactor(vector<vector<int>> &a, vector<vector<int>> &temp, int p, int q, int n){
    int i = 0, j = 0;

    for (int row = 0; row < n; row++){
        for (int col = 0; col < n; col++){
            if (row != p && col != q){
                temp[i][j++] = a[row][col];
                if (j == n - 1){
                    j = 0;
                    i++;
                }
            }
        }
    }
}

// calculates determinant of a matrix 'a'
int calculateDeterminant(vector<vector<int>> &a, int n, int N){
    int D = 0;
    if (n == 1)
        return a[0][0];
    vector<vector<int>> temp(N, vector<int>(N));
    int sign = 1;
    for (int f = 0; f < n; f++){
        getCofactor(a, temp, 0, f, n);
        D += sign * a[0][f] * calculateDeterminant(temp, n - 1, N);
        sign = -sign;
    }
    return D;
}

// calculates adjoint matrix 'adj' of a matrix 'a' using recursion
void getAdjoint(vector<vector<int>> &a, vector<vector<int>> &adj, int N){
    if (N == 1){
        adj[0][0] = 1;
        return;
    }
	
    int sign = 1;
    vector<vector<int>> temp(N, vector<int>(N));
    for (int i = 0; i < N; i++){
        for (int j = 0; j < N; j++){
            getCofactor(a, temp, i, j, N);
            sign = ((i + j) % 2 == 0) ? 1 : -1;
            adj[j][i] = (sign) * (calculateDeterminant(temp, N - 1, N));
        }
    }
}

bool calculateInverse(vector<vector<int>> &a, vector<vector<int>> &inv, int N)
{
    int det = calculateDeterminant(a, N, N);
    if (det == 0){
        cout << "Inverse does not exist";
        return false;
    }
	
    int invDet = modInverse(det, 26);
    cout << det % 26 << " #### " << invDet << '\n';
    vector<vector<int>> adj(N, vector<int>(N));
    getAdjoint(a, adj, N);
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            inv[i][j] = (adj[i][j] * invDet) % 26;
    return true;
}

void performDecryption(){
    int x, y, i, j, k, n;
    cout << "Enter the decryption key: ";
    string key;
    cin >> key;
    n = sqrt(key.length());
    vector<vector<int>> a(n, vector<int>(n));
    vector<vector<int>> adj(n, vector<int>(n));
    vector<vector<int>> inv(n, vector<int>(n));
    int iter = 0;
    for (i = 0; i < n; i++){
        for (j = 0; j < n; j++){
            int val = key[iter] - 97;
            a[i][j] = val;
            iter++;
        }
    }
    if (calculateInverse(a, inv, n)){
        cout << "Inverse exists\n";
    }
    cout << "Enter the message to decrypt\n";
    string message;
    cin >> message;
    k = 0;
    string decryptedText = "";
    while (k < message.size()){
        for (i = 0; i < n; i++){
            int sum = 0;
            int temp = k;
            for (j = 0; j < n; j++){
                sum += ((inv[i][j] + 26) % 26 * (message[temp++] - 'a') % 26) % 26;
                sum = sum % 26;
            }
            sum += 'a';
            decryptedText += sum;
        }
        k += n;
    }
    int lastCharIndex = decryptedText.size() - 1;
    while (decryptedText[lastCharIndex] == 'x'){
        lastCharIndex--;
    }
    cout << "\nDecrypted text is: ";
    for (i = 0; i <= lastCharIndex; i++){
        cout << decryptedText[i];
    }
    cout << '\n';
}

int main(){
    int choice;
    cout << "Enter your choice :\n";
    cout << "1. Encryption:\n2.Decryption:\n";
    cin >> choice;

    switch (choice){
    case 1:
        performEncryption();
        break;
    case 2:
        performDecryption();
        break;
    }
}

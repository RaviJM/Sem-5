#include <iostream> 
using namespace std;

int main(){
    char arr[3][3] = {0};
    for (int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            cout<<arr[i][j]<<" ";
        }
        cout<<"\n";
    }
    return 0;
}
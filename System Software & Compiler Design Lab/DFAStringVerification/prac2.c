// checking if string is valid or not using DFA Transition Table
// for DFA-> if string starts with digit, it is invalid, and valid if it starts with alphabet
#include <stdio.h>
#include <string.h>

int main(){


    //making transition table
    int rows, columns;
    printf("Enter no. of row(no. of states)(including dead state): ");
    scanf("%d", &rows);
    printf("Enter no. of columns(no. of input symbols): ");
    scanf("%d", &columns);

    int transitionTable[rows][columns];
    
    for (int i=0;i<rows;i++){
        for (int j=0;j<columns;j++){
            printf("Enter value[%d][%d]: ",i,j);
            fflush(stdin);
            scanf("%d", &transitionTable[i][j]);
        }
    }


    //taking accepted states as input
    printf("Enter number of accepted states: ");
    int noOfAcceptedStates;
    fflush(stdin);
    scanf("%d", &noOfAcceptedStates);

    int acceptedStates[noOfAcceptedStates];
    for (int i=0;i<noOfAcceptedStates;i++){
        printf("Enter accepted state-%d: ",(i+1));
        fflush(stdin);
        scanf("%d", &acceptedStates[i]);
    }
    

    //taking string as input and converting into second string (i.e. lllldd)
    char st1[50];
    char st2[50];

    printf("Enter String: ");
    fflush(stdin);
    gets(st1);

    for (int i=0;i<strlen(st1);i++){
        if ((st1[i] >= 65 && st1[i] <= 90) || (st1[i] >= 97 && st1[i] <= 122)){
            st2[i] = 'l';
        }
        else if (st1[i] >= 48 && st1[i] <= 57){
            st2[i] = 'd';
        }
    }


    //Actual Process(checking if string is valid or not)
    int row = 0;
    int col = 0;
    // traversing the second string
    for (int i=0;i<strlen(st1);i++){
        if (st2[i] == 'l'){
            col = 0;
        }
        else if (st2[i] == 'd'){
            col = 1;
        }
        row = transitionTable[row][col];
    }
    int finalState = transitionTable[row][col];

    //checking if final state lies in the set of accepted states or not
    int flag = 0;
    for (int i=0;i<noOfAcceptedStates;i++){
        if (acceptedStates[i] == finalState){
            flag = 1;
            break;
        }
    }
    if (flag == 1){
        printf("String is Accepted!");
    }
    else{
        printf("String is Invalid.");
    }
}
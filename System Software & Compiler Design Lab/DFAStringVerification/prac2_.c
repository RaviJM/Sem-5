// checking if string is valid or not using DFA Transition Table
// for DFA-> Generalised DFA for alphabets a,b,c...
// DO NOT use uppercase alphabets(symbols) for this program
// start using lowercase alphabets(symbols) from 'a' onwards.
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
    

    //taking string as input
    char st1[50];

    printf("Enter String: ");
    fflush(stdin);
    gets(st1);


    //Actual Process(checking if string is valid or not)
    int row = 0;
    int col = 0;

    int flag1 = 1;  //to check if there is no other alphabet than sigma
    // traversing the string
    for (int i=0;i<strlen(st1);i++){
        col = st1[i] - 97;
        if (col >= columns){ //i.e. alphabet does not belong to signma
            col = 0;
            flag1 = 0;
            break;
        }
        row = transitionTable[row][col];
    }
    int finalState = transitionTable[row][col];

    //checking if final state lies in the set of accepted states or not
    int flag2 = 0;
    for (int i=0;i<noOfAcceptedStates;i++){
        if (acceptedStates[i] == finalState){
            flag2 = 1;
            break;
        }
    }
    if (flag1 == 1 && flag2 == 1){
        printf("String is Accepted!");
    }
    else{
        printf("String is Invalid.");
    }
}
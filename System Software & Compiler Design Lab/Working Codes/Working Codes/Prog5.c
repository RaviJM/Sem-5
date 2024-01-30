#include <stdio.h>
#include <stdbool.h>
#include <string.h>

#define MAX_SYMBOLS 10

char nonTerminals[] = "SAB";
char terminals[] = "ab";
char productions[][10] = {"S->aAb", "S->B", "A->a", "A->null", "B->b"};

bool isTerminal(char symbol)
{
    for (int i = 0; terminals[i]; i++)
    {
        if (terminals[i] == symbol)
        {
            return true;
        }
    }
    return false;
}

void addToSet(char set[], char symbol)
{
    if (strchr(set, symbol) == NULL)
    {
        strncat(set, &symbol, 1);
    }
}

void calculateFirst(char nonTerminal, char first[])
{
    for (int i = 0; productions[i][0]; i++)
    {
        if (productions[i][0] == nonTerminal)
        {
            int j = 3;
            while (productions[i][j] != '\0')
            {
                if (isTerminal(productions[i][j]))
                {
                    addToSet(first, productions[i][j]);
                    break;
                }
                else if (productions[i][j] != 'null') // Change "null" to 'null'
                {
                    calculateFirst(productions[i][j], first);
                    if (!strchr(first, 'null')) // Change "null" to 'null'
                    {
                        break;
                    }
                }
                j++;
            }
        }
    }
}

void calculateFollow(char nonTerminal, char follow[])
{
    if (nonTerminal == 'S')
    {
        // Start symbol
        addToSet(follow, '$');
    }
    for (int i = 0; productions[i][0]; i++)
    {
        for (int j = 3; productions[i][j]; j++)
        {
            if (productions[i][j] == nonTerminal)
            {
                int k = j + 1;
                while (productions[i][k] != '\0')
                {
                    if (isTerminal(productions[i][k]))
                    {
                        addToSet(follow, productions[i][k]);
                        break;
                    }
                    else
                    {
                        char first[MAX_SYMBOLS] = {0};
                        calculateFirst(productions[i][k], first);
                        bool epsilonFound = false;
                        for (int m = 0; first[m]; m++)
                        {
                            if (first[m] == 'null') // Change "null" to 'null'
                            {
                                epsilonFound = true;
                            }
                            else
                            {
                                addToSet(follow, first[m]);
                            }
                        }
                        if (!epsilonFound)
                        {
                            break;
                        }
                    }
                    k++;
                }
                if (productions[i][k] == '\0')
                {
                    if (productions[i][0] != nonTerminal)
                    {
                        calculateFollow(productions[i][0], follow);
                    }
                }
            }
        }
    }
}

int main()
{
    char first[MAX_SYMBOLS] = {0};
    char follow[MAX_SYMBOLS] = {0};
    for (int i = 0; nonTerminals[i]; i++)
    {
        calculateFirst(nonTerminals[i], first);
    }
    for (int i = 0; nonTerminals[i]; i++)
    {
        calculateFollow(nonTerminals[i], follow);
    }
    printf("\nFIRST sets:\n");
    for (int i = 0; nonTerminals[i]; i++)
    {
        printf("FIRST(%c) = {%s}\n", nonTerminals[i], first);
        first[0] = '\0'; // Clear FIRST set for the next non-terminal
    }
    printf("\nFOLLOW sets:\n");
    for (int i = 0; nonTerminals[i]; i++)
    {
        printf("FOLLOW(%c) = {%s}\n", nonTerminals[i], follow);
        follow[0] = '\0'; // Clear FOLLOW set for the next non-terminal
    }
    return 0;
}

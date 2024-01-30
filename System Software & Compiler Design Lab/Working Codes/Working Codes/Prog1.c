#include <stdio.h>
#include <string.h>
#include <ctype.h>
#define MAX_IDENTIFIERS 100
const char *keywords[] = {
    "auto", "break", "case", "char", "const", "continue", "default",
    "do", "double", "else", "enum", "extern", "float", "for", "goto",
    "if", "int", "long", "register", "return", "short", "signed", "sizeof",
    "static", "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while"};
int is_keyword(const char *word)
{
    for (int i = 0; i < sizeof(keywords) / sizeof(keywords[0]); i++)
    {
        if (strcmp(word, keywords[i]) == 0)
        {
            return 1;
        }
    }
    return 0;
}
int main()
{
    char identifier[MAX_IDENTIFIERS][50];
    int numIdentifiers = 0;
    FILE *file = fopen("Prog0.c", "r");
    char word[50];
    while (fscanf(file, "%s", word) != EOF)
    {
        if (is_keyword(word) == 1)
        {
            printf("Keyword: %s\n", word);
        }
        else if (isalpha(word[0]))
        {
            int found = 0;
            for (int i = 0; i < numIdentifiers; i++)
            {
                if (strcmp(word, identifier[i]) == 0)
                {
                    found = 1;
                    break;
                }
            }
            if (!found)
            {
                strcpy(identifier[numIdentifiers], word);
                printf("Identifier: %s\n", identifier[numIdentifiers]);
                numIdentifiers++;
                if (numIdentifiers == MAX_IDENTIFIERS)
                {
                    printf("Maximum number of identifiers reached.\n");
                    break;
                }
            }
        }
    }
    fclose(file);
    return 0;
}

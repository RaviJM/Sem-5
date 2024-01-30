#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

// Function to check if a word is a keyword
int isKeyword(const char *word) {
    char keywords[][20] = {
        "auto", "break", "case", "char", "const", "continue", "default", "do",
        "double", "else", "enum", "extern", "float", "for", "goto", "if", "int",
        "long", "register", "return", "short", "signed", "sizeof", "static", "struct",
        "switch", "typedef", "union", "unsigned", "void", "volatile", "while"
    };

    for (int i = 0; i < sizeof(keywords) / sizeof(keywords[0]); i++) {
        if (strcmp(word, keywords[i]) == 0) {
            return 1; // Found as a keyword
        }
    }
    return 0; // Not a keyword
}

// Function to check if a word is an identifier
int isIdentifier(const char *word) {
    if ((word[0] >= 'a' && word[0] <= 'z') || (word[0] >= 'A' && word[0] <= 'Z') || word[0] == '_') {
        // Check the rest of the characters in the word
        for (int i = 1; i < strlen(word); i++) {
            if (!((word[i] >= 'a' && word[i] <= 'z') || (word[i] >= 'A' && word[i] <= 'Z')
                  || (word[i] >= '0' && word[i] <= '9') || word[i] == '_')) {
                return 0; // Not a valid identifier
            }
        }
        return 1; // Valid identifier
    }
    return 0; // Not an identifier
}
// Function to check if a word is a string literal
bool isStringLiteral(const char *word) {
    return (word[0] == '"' && word[strlen(word) - 1] == '"');
}

// Function to check if a word is a number
bool isNumber(const char *word) {
    char *endptr;
    strtod(word, &endptr);
    return (*endptr == '\0'); // If endptr points to the null terminator, it's a valid number.
}

int main() {
    FILE *file = fopen("input.c", "r");
    if (file == NULL) {
        printf("Error opening the file.\n");
        return 1;
    }

    char word[100];
    while (fscanf(file, "%s", word) == 1) {
        // Check if the word is a keyword
        if (isKeyword(word)) {
            printf("%s is a keyword.\n", word);
        }
        // Check if the word is an identifier
        else if (isIdentifier(word)) {
            printf("%s is an identifier.\n", word);
        }
        // Check if the word is a string literal
        else if (isStringLiteral(word)) {
            printf("%s is a string literal.\n", word);
        }
        // Check if the word is a number
        else if (isNumber(word)) {
            printf("%s is a number.\n", word);
        }
        // If not a keyword, identifier, string literal, or number, classify as others
        else {
            printf("%s is classified as others.\n", word);
        }
    }

    fclose(file);
    return 0;
}
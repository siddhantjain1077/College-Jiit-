#include <stdio.h>
#include <ctype.h>

void countVowelsAndConsonants(const char *str, int *vowels, int *consonants) {
    *vowels = 0;
    *consonants = 0;

    while (*str != '\0') {
        char lowercaseChar = tolower(*str);

        if (lowercaseChar == 'a' || lowercaseChar == 'e' || lowercaseChar == 'i' || lowercaseChar == 'o' || lowercaseChar == 'u') {
            (*vowels)++;
        } else if ((lowercaseChar >= 'a' && lowercaseChar <= 'z')) {
            
            (*consonants)++;
        }

        str++;
    }
}

int main() {
    char inputString[100];

    printf("Enter a string: ");
    fgets(inputString, sizeof(inputString), stdin);

    if (inputString[strlen(inputString) - 1] == '\n') {
        inputString[strlen(inputString) - 1] = '\0';
    }

    int vowelCount, consonantCount;

    countVowelsAndConsonants(inputString, &vowelCount, &consonantCount);

    printf("Number of vowels: %d\n", vowelCount);
    printf("Number of consonants: %d\n", consonantCount);

    return 0;
}

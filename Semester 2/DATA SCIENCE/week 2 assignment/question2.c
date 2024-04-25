#include<stdio.h>

void countFrequency(char str[]){
    int count[26] = {0};

    for (int i = 0; str[i] !='\0'; i++)
    { 
        if (str[i]>= 'a' && str[i] <= 'z')
        {
            count[str[i] - 'a']++;
        }
    }

    // printf();
    
}
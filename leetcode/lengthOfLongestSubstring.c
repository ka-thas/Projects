#include <string.h>
#include <stdio.h>

int lengthOfLongestSubstring(char *s)
{
    int max_length = 0; // return value
    int first_index = 0;
    int last_index = 0;
    for (int i = 0; i < strlen(s); i++)
    {
        printf("-- %c\n", s[i]);
        last_index = i;
        for (int j = first_index; j < last_index; j++)
        {
            printf("%c\n", s[j]);
            if (s[i] == s[j])
            {
                first_index = j;
                break;
            }
        }

        if (1 + last_index - first_index > max_length)
        {
            max_length = last_index - first_index;
        }
    }
    return max_length;
}

// abcabcbb
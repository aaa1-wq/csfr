#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
    char fname1[100];
    printf("Enter the file name£º");
    gets(fname1);
    FILE* fp1 = fopen(fname1, "r");
    if (fp1 == NULL)
	{
        printf("Can¡¯t open file \"%s\".", fname1);
        return 1;
    }
    char fname2[110];
    strcpy(fname2, fname1);
    int i = 0, j = 0, flag = 0;
    while (1)
    {
    	if (fname2[i] == '.')
    	{
    		if (fname2[i + 1] == 'p')
    			flag = 1;
			fname2[i++] = '_';
			fname2[i++] = '2';
			fname2[i++] = '3';
			fname2[i++] = '3';
			fname2[i++] = '0';
			fname2[i++] = '7';
			fname2[i++] = '1';
			fname2[i++] = '3';
			fname2[i++] = '0';
			fname2[i++] = '1';
			fname2[i++] = '4';
			fname2[i++] = '5';
			fname2[i++] = '.';
			if (flag == 0)
			{
				fname2[i++] = 'c';
				fname2[i++] = 'p';
				fname2[i++] = 'p';
			}
			else
			{
				fname2[i++] = 'p';
				fname2[i++] = 'y';
			}
			fname2[i] = '\0';
			break;
		}
    	i++;
	}
    FILE* fp2 = fopen(fname2, "w");
    char line[200];
    int linen = 1;
    while (fgets(line, sizeof(line), fp1))
	{
        int flag1 = 1, i;
        for (i = 0; i < strlen(line); i++)
		{
            if (line[i] != ' ' && line[i] != '\t' && line[i] != '\n' && line[i] != '\r')
			{
                flag1 = 0;
                break;
            }
        }        
        int flag2 = 0;
        if ((flag == 0 && line[0] == '/' && line[1] == '/') || (flag == 1 && line[0] == '#'))
            flag2 = 1;
        if (!flag1 && !flag2)
		{
            fprintf(fp2, "%d %s", linen, line);
            linen++;
        }
		else
            fprintf(fp2, "%s", line);
    }
    fclose(fp1);
    fclose(fp2);
    printf("End of Comment.");
    return 0;
}

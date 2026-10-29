#include<stdio.h>
#define MAX_LEN 100
int main()
{
    char a[MAX_LEN], b[MAX_LEN];
    int key, n, i, j, flag = 0, k;
    printf("Enter a line of text: \n");
    gets(a);
    n = strlen(a);
    for (i = 0; i <= n; i++)
    	b[i] = '\0';
    printf("Enter the key: ");
    scanf("%d", &key);
    j = 0;
    for (i = 0; i < n; i++)
    {
    	k = 0;
    	while (k != key)
    	{
    		if (b[j] == '\0')
    			k++;
			if (k == key)
				b[j] = a[flag++];
			j = (j + 1) % n;
		}
	}
	printf("The cipher text:\n");
	printf("%s", b); 
    return 0;
}

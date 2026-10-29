#include<stdio.h>
#include<string.h>
int main()
{
	char a[105], b[105], c[105], d[105], *flag1, *flag2;
	printf("Enter 3 strings(length < 100):\n");
	gets(a);
	gets(b);
	gets(c);
	int n = strlen(c), i, j, len = n, *sta, flag3 = 0;
	while (len)
	{
		for (i = 0; i <= n - len; i++)
		{
			for (j = 0; j < len; j++)
				d[j] = c[i + j];
			d[j] = '\0';
			flag1 = strstr(a, d);
			flag2 = strstr(b, d);
			if (flag1 != NULL && flag2 != NULL)
			{
				flag3 = 1;
				break;
			}
				
		}
		if (flag3 == 1)
			break;
		len--;
	}
	if (flag3 == 0)
		printf("There is no common substring!");
	else
	{
		printf("Their longest common substring is:\n");
		for (i = 0; i < j; i++)
			printf("%c", *(flag1 + i));
	}
	return 0;
}

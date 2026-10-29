#include<stdio.h>
#include<string.h>
#define maxn 105
int main()
{
	char a[maxn], *p, *q, b[maxn];
	int flag1 = 0, flag2 = 0;
	printf("Enter a string with extra white spaces:\n");
	gets(a);
	for(p = a, q = b; *p; p++)
	{
		if (*p == ' ')
		{
			if (flag1 == 0)
				continue;
			else if (flag2 == 0)
			{
				flag2 = 1;
				*q++ = *p;
			}
			else
				continue;
		}
		else
		{
			flag1 = 1;
			if (flag2 == 1)
				flag2 = 0;
			*q++ = *p;
		}
	}
	*q = '\0';
	printf("The string after removing extra whitespaces:\n");
	puts(b);
	return 0;
}

#include<stdio.h>
char a[105], b[105], c[105];
int get_ina()
{
	int i = 0;
	while (1)
	{
		scanf("%c", &a[i++]);
		if (a[i - 1] == '\n')
			return i - 1;
	}
}
int get_inb()
{
	int i = 0;
	while (1)
	{
		scanf("%c", &b[i++]);
		if (b[i - 1] == '\n')
			return i - 1;
	}
}
int main()
{
	printf("Enter 2 strings (length < 100): \n");
	int n, m, i, j, low, high, length = 0, len = 0;
	n = get_ina();
	m = get_inb();
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < m; j++)
		{
			if (a[i] == b[j])
			{
				len = 0;
				int k = i, q = j;
				while (a[k] == b[q] && k < n && q < m)
				{
					len++;
					k++;
					q++;
				}
				if (len > length)
				{
					low = i;
					high = k;
					length = len;
				}
				j = q - 1;
			}
		}
	}
	if (len == 0)
		printf("There is no common character.");
	else
	{
		printf("The longest common substring is: \n");
		for (i = low; i < high; i++)
			printf("%c", a[i]); 
	}
}

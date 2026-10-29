#include<stdio.h>
int main()
{
	int a[100], n = 0, i, j;
	char x;
	printf("Enter an integer n (1 <= n < 10^100): ");
	while (1)
	{
		scanf("%c", &x);
		if (x == '\n')
			break;
		a[++n] = x - '0';
	}
	for (i = n; i > 1; i--)
	{
		if (a[i] > a[i - 1])
		{
			for (j = n; j > i - 1; j--)
			{
				if (a[j] > a[i - 1])
				{
					int temp;
					temp = a[j];
					a[j] = a[i - 1];
					a[i - 1] = temp;
					int end = n, pos;
					while (end > i)
					{
						for (pos = j = i; j < end; j++)
							if (a[j] > a[j + 1])
							{
								int temp;
								temp = a[j];
								a[j] = a[j + 1];
								a[j + 1] = temp;
								pos = j;
							}
						end = pos;
					}
					printf("The larger smallest integer is: ");
					for (i = 1; i <= n; i++)
						printf("%d", a[i]);
					return 0;
				}
			}
		}
	}
	printf("No larger integer exists!");
	return 0;
}

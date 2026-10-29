#include<stdio.h>
int main()
{
	int n, i, j;
	printf("Enter n: ");
	scanf("%d", &n);
	if (n != 1)
	{
		for (i = 1; i <= 2 * n - 1; i++)
			printf("* ");
		printf("\n");
	}
	for (i = 2; i <= n - 1; i++)
	{
		for (j = 1; j <= 2 * i - 2; j++)
			printf(" ");
		printf("*");
		for (j = 1; j <= (2 * n - 1 - 2 * i) * 2 + 1; j++)
			printf(" ");
		printf("*\n");
	}
	for (i = 1; i <= n * 2 - 2; i++)
		printf(" ");
	printf("*");
	return 0;
}

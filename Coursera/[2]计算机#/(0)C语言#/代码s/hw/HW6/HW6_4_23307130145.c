#include<stdio.h>
int main()
{
	int n, a[31][31], i, j, x, d;
	printf("Enter n (n<=30): ");
	scanf("%d", &n);
	for (x = d = 1; d <= 2 * n - 1; d++)
	{
		if (d <= n)
		{
			if (d % 2 == 0)
				for (i = d - 1, j = 0; j < d; i--, j++)
					a[i][j] = x++;
			else
				for (i = 0, j = d - 1; i < d; i++, j--)
					a[i][j] = x++;
		}
		else
		{
			if (d % 2 == 0)
				for (i = n - 1, j = d - n; j < n; i--, j++)
					a[i][j] = x++;
			else
				for (i = d - n, j = n - 1; i < n; i++, j--)
					a[i][j] = x++;
		}
	}
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < n; j++)
			printf("%4d", a[i][j]);
		if (i != n - 1)
			printf("\n");
	}
	return 0;
}

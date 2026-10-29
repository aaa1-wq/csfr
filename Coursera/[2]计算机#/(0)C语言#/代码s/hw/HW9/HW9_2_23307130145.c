#include<stdio.h>
int a[200];
int mul(int m)
{
	int j, x = 0, k = a[0];
	for (j = k; j; j--)
	{
		a[j] *= m;
		if (a[j] > 9)
		{
			int p = j;
			while (a[p] > 9)
			{
				a[p + 1] += a[p] / 10;
				a[p++] %= 10;
				
			}
			if (p > a[0])
				a[0] = p;
		}	
	}
}
int main()
{
	printf("Enter n: ");
	int n, i;
	scanf("%d", &n);
	a[0] = a[1] = 1;
	for (i = 2; i <= n; i++)
		mul(i);
	printf("%d! = ", n);
	for (i = a[0]; i ; i--)
		printf("%d", a[i]);
	printf("\nIt's a %d-digit number.", a[0]);
	return 0;
}

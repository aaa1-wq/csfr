#include<stdio.h>
int judge(int x, int *a, int *b)
{
	int m = 10;
	while (m < x)
	{
		*a = x / m;
		*b = x % m;
		if ( (*b + *a) * (*b + *a) == x)
			return 1;
		m *= 10;
	}
	return 0;
}
int main()
{
	int n, i, a, b;
	printf("Enter n ([10, 1000000]): ");
	scanf("%d",&n);
	printf("K-numbers within %d:\n", n);
	for (i = 10; i < n; i++)
		if (judge(i, &a, &b))
			printf("%d=(%d+%d)^2\n", i, a, b);
	return 0;
}

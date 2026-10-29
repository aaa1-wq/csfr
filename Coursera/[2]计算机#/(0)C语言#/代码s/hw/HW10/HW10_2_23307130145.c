#include<stdio.h>
void judge(int x)
{
	int a, b, m = 10;
	while (m < x)
	{
		a = x / m;
		b = x % m;
		if ( (b + a) * (b + a) == x)
		{
			printf("%d=(%d+%d)^2\n", x, a, b);
			return;
		}
		m *= 10;
	}
	return;
}
int main()
{
	int n, i;
	printf("Enter n ([10, 1000000]): ");
	scanf("%d",&n);
	printf("K-numbers within %d:\n", n);
	for (i = 10; i <= n; i++)
		judge(i);
	return 0;
}

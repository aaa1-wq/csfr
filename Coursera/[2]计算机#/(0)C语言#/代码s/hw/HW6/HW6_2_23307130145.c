#include<stdio.h>
int main()
{
	int n, i = 2;
	printf("Enter a positive integer n (1 <= n <= 2147483647): ");
	scanf("%d", &n);
	if (n == 1)
	{
		printf("1 = 1");
		return 0;
	}
	printf("%d = ", n);
	while (n != 1)
	{
		while (n % i == 0)
		{
			n /= i;
			printf("%d ", i);
			if (n != 1)
				printf("* ");
		}
		i++;
	}
	return 0;
}

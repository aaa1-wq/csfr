#include<stdio.h>
int main()
{
	int a, flag = 0, b;
	printf("Enter an integer: ");
	scanf("%d", &a);
	printf("The reversal is: ");
	while (a)
	{
		b = a % 10;
		a /= 10;
		if (b && flag == 0)
			flag = 1;
		if (flag == 0)
			continue;
		printf("%d", b);
	}
	return 0;
}

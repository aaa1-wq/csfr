#include<stdio.h>
int main()
{
	int a, b, c, d, sum1, sum2;
	printf("Enter 2 fractions separated by a plus sign: ");
	scanf("%d/%d+%d/%d", &a, &b, &c, &d);
	sum1 = a * d + b * c;
	sum2 = b * d;
	int i = sum1 < sum2 ? sum1 : sum2;
	while (i > 1)
	{
		if (sum1 % i == 0 && sum2 % i == 0)
		{
			sum1 /= i;
			sum2 /= i;
			continue;
		}
		i--;
	}
	if (sum2 == 1)
		printf("%d/%d+%d/%d=%d", a, b, c, d, sum1);
	else
		printf("%d/%d+%d/%d=%d/%d", a, b, c, d, sum1, sum2);
	return 0;
}
